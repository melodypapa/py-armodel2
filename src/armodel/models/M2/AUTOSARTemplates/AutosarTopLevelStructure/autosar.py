"""AUTOSAR AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 298)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 287)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 59)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 968)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1993)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 203)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 30)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 42)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 71)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 29)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 56)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AutosarTopLevelStructure.classes.json"""

from __future__ import annotations
import threading
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.serialization.name_converter import NameConverter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.file_info_comment import (
    FileInfoComment,
)


class AUTOSAR(ARObject):
    """AUTOSAR AUTOSAR root element.

    This is the root element of any ARXML document. As the root element,
    it handles namespace attributes that should appear only once in the document.

    This class implements the singleton pattern to ensure only one AUTOSAR instance
    exists throughout the application. Use AUTOSAR.reset() to clear the singleton
    for testing purposes.
    """

    # Singleton instance variables
    _instance: Optional["AUTOSAR"] = None
    _initialized: bool = False
    _lock: threading.Lock = threading.Lock()

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    admin_data: Optional[AdminData]
    ar_packages: list[ARPackage]
    file_info_comment: Optional[FileInfoComment]
    introduction: Optional[DocumentationBlock]
    schema_location: Optional[str]

    def __new__(cls) -> "AUTOSAR":
        """Create or return the singleton instance.

        Uses double-checked locking for thread safety.

        Returns:
            The singleton AUTOSAR instance
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        """Initialize AUTOSAR.

        Only initializes once due to singleton pattern.
        """
        if self._initialized:
            return

        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.ar_packages: list[ARPackage] = []
        self.file_info_comment: Optional[FileInfoComment] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.schema_location: Optional[str] = None

        self._initialized = True

    def clear(self) -> None:
        """Clear all state from the AUTOSAR instance.

        This method resets the instance's state while keeping the singleton alive.
        This is useful for reusing the singleton for different operations without
        resetting the singleton instance itself.

        Example:
            autosar = AUTOSAR()
            reader.load_arxml(autosar, "file1.arxml")
            autosar.clear()  # Clear state for next operation
            reader.load_arxml(autosar, "file2.arxml")
        """
        self.admin_data = None
        self.ar_packages = []
        self.file_info_comment = None
        self.introduction = None
        self.schema_location = None

    @classmethod
    def reset(cls) -> None:
        """Reset the singleton instance.

        This is primarily intended for testing to ensure test isolation.
        After calling reset(), the next AUTOSAR() call will create a fresh instance.

        Warning:
            Do not use this in production code as it can lead to unexpected behavior
            if multiple parts of the application rely on the singleton instance.

        Example:
            def setUp(self):
                AUTOSAR.reset()  # Ensure clean state for each test
                self.autosar = AUTOSAR()
        """
        with cls._lock:
            cls._instance = None
            cls._initialized = False

    def serialize(self) -> ET.Element:
        """Serialize AUTOSAR to XML element.

        Override base class to handle namespace attributes and preserve schema location.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Add AUTOSAR namespace attributes if this is an AUTOSAR instance (root element only)
        elem.set("xmlns", "http://autosar.org/schema/r4.0")
        elem.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

        # Use stored schema location or fallback to default
        if self.schema_location is not None:
            elem.set("xsi:schemaLocation", self.schema_location)
        else:
            # Fallback to default schema location
            elem.set("xsi:schemaLocation", "http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd")

        # Serialize admin_data
        if self.admin_data is not None:
            serialized = self.admin_data.serialize()
            elem.append(serialized)

        # Serialize file_info_comment
        if self.file_info_comment is not None:
            serialized = self.file_info_comment.serialize()
            elem.append(serialized)

        # Serialize introduction
        if self.introduction is not None:
            serialized = self.introduction.serialize()
            elem.append(serialized)

        # Serialize ar_packages (list to container "AR-PACKAGES")
        if self.ar_packages:
            wrapper = ET.Element("AR-PACKAGES")
            for item in self.ar_packages:
                serialized = item.serialize()
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AUTOSAR":
        """Deserialize XML element to AUTOSAR object.

        Override base class to extract schema location from xsi:schemaLocation attribute.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AUTOSAR object (singleton instance)
        """
        # Get or create singleton instance
        obj = cls()

        # Extract schema location from xsi:schemaLocation attribute
        schema_loc = element.get("{http://www.w3.org/2001/XMLSchema-instance}schemaLocation")
        if schema_loc is not None:
            obj.schema_location = schema_loc

        # Parse admin_data
        child = SerializationHelper.find_child_element(element, "ADMIN-DATA")
        if child is not None:
            from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import AdminData
            admin_data_value = AdminData.deserialize(child)
            obj.admin_data = admin_data_value

        # Parse file_info_comment
        child = SerializationHelper.find_child_element(element, "FILE-INFO-COMMENT")
        if child is not None:
            from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.file_info_comment import FileInfoComment
            file_info_comment_value = FileInfoComment.deserialize(child)
            obj.file_info_comment = file_info_comment_value

        # Parse introduction
        child = SerializationHelper.find_child_element(element, "INTRODUCTION")
        if child is not None:
            from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import DocumentationBlock
            introduction_value = DocumentationBlock.deserialize(child)
            obj.introduction = introduction_value

        # Parse ar_packages (list from container "AR-PACKAGES")
        obj.ar_packages = []
        container = SerializationHelper.find_child_element(element, "AR-PACKAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                from armodel.serialization.model_factory import ModelFactory
                factory = ModelFactory()
                tag = SerializationHelper.strip_namespace(child.tag)
                child_class = factory.get_class(tag)
                if child_class is not None:
                    child_value = child_class.deserialize(child)
                    obj.ar_packages.append(child_value)

        return obj


class AUTOSARBuilder:
    """Builder for AUTOSAR."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AUTOSAR = AUTOSAR()

    def clear(self) -> "AUTOSARBuilder":
        """Clear the AUTOSAR instance.

        Returns:
            This builder for method chaining
        """
        self._obj.clear()
        return self

    def build(self) -> AUTOSAR:
        """Build and return AUTOSAR object.

        Returns:
            AUTOSAR instance (singleton)
        """
        # TODO: Add validation
        return self._obj