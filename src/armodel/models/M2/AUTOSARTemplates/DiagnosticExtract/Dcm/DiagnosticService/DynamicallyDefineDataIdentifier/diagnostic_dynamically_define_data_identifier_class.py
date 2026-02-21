"""DiagnosticDynamicallyDefineDataIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DynamicallyDefineData import (
    DiagnosticHandleDDDIConfigurationEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    check_per: Optional[Boolean]
    configuration: Optional[DiagnosticHandleDDDIConfigurationEnum]
    subfunctions: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifierClass."""
        super().__init__()
        self.check_per: Optional[Boolean] = None
        self.configuration: Optional[DiagnosticHandleDDDIConfigurationEnum] = None
        self.subfunctions: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDynamicallyDefineDataIdentifierClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDynamicallyDefineDataIdentifierClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize check_per
        if self.check_per is not None:
            serialized = ARObject._serialize_item(self.check_per, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHECK-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize configuration
        if self.configuration is not None:
            serialized = ARObject._serialize_item(self.configuration, "DiagnosticHandleDDDIConfigurationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subfunctions (list to container "SUBFUNCTIONS")
        if self.subfunctions:
            wrapper = ET.Element("SUBFUNCTIONS")
            for item in self.subfunctions:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """Deserialize XML element to DiagnosticDynamicallyDefineDataIdentifierClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDynamicallyDefineDataIdentifierClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDynamicallyDefineDataIdentifierClass, cls).deserialize(element)

        # Parse check_per
        child = ARObject._find_child_element(element, "CHECK-PER")
        if child is not None:
            check_per_value = child.text
            obj.check_per = check_per_value

        # Parse configuration
        child = ARObject._find_child_element(element, "CONFIGURATION")
        if child is not None:
            configuration_value = DiagnosticHandleDDDIConfigurationEnum.deserialize(child)
            obj.configuration = configuration_value

        # Parse subfunctions (list from container "SUBFUNCTIONS")
        obj.subfunctions = []
        container = ARObject._find_child_element(element, "SUBFUNCTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.subfunctions.append(child_value)

        return obj



class DiagnosticDynamicallyDefineDataIdentifierClassBuilder:
    """Builder for DiagnosticDynamicallyDefineDataIdentifierClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDynamicallyDefineDataIdentifierClass = DiagnosticDynamicallyDefineDataIdentifierClass()

    def build(self) -> DiagnosticDynamicallyDefineDataIdentifierClass:
        """Build and return DiagnosticDynamicallyDefineDataIdentifierClass object.

        Returns:
            DiagnosticDynamicallyDefineDataIdentifierClass instance
        """
        # TODO: Add validation
        return self._obj
