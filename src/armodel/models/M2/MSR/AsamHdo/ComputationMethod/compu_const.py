"""CompuConst AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.serialization.name_converter import NameConverter
from armodel.serialization.model_factory import ModelFactory


class CompuConst(ARObject):
    """AUTOSAR CompuConst."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_const_content_type: Optional[CompuConstContent]
    def __init__(self) -> None:
        """Initialize CompuConst."""
        super().__init__()
        self.compu_const_content_type: Optional[CompuConstContent] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuConst to XML element.

        Handles CompuConstContent polymorphic types by serializing them directly.
        Since CompuConstContent is abstract, we serialize the concrete subclass
        (e.g., CompuConstTextContent) without a wrapper element.

        Returns:
            xml.etree.ElementTree.Element representing this CompuConst
        """
        tag = NameConverter.to_xml_tag(self.__class__.__name__)
        elem = ET.Element(tag)

        # Serialize compu_const_content_type (polymorphic CompuConstContent subclass)
        if self.compu_const_content_type is not None:
            serialized = self.compu_const_content_type.serialize()
            # Append the entire serialized element (not just children)
            # This preserves the correct XML structure for CompuConstTextContent
            elem.append(serialized)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML element to CompuConst.

        Handles CompuConstContent polymorphic types by using ModelFactory to resolve
        concrete subclasses like CompuConstTextContent. This ensures CompuConst.compu_const_content_type
        is properly populated with the correct concrete subclass.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuConst instance with compu_const_content_type properly set
        """
        obj = cls.__new__(cls)
        obj.__init__()

        # Use ModelFactory for polymorphic type resolution
        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        # Find child elements that are CompuConstContent subclasses
        for child in element:
            child_tag = SerializationHelper.strip_namespace(child.tag)
            concrete_class = factory.get_class(child_tag)

            if concrete_class:
                # Import base class for type checking
                from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import CompuConstContent

                # Check if it's a CompuConstContent subclass (for compu_const_content_type)
                if isinstance(concrete_class, type) and issubclass(concrete_class, CompuConstContent):
                    obj.compu_const_content_type = SerializationHelper.unwrap_primitive(concrete_class.deserialize(child))
                    break  # Only one content type expected

        return obj


class CompuConstBuilder:
    """Builder for CompuConst."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConst = CompuConst()

    def build(self) -> CompuConst:
        """Build and return CompuConst object.

        Returns:
            CompuConst instance
        """
        # TODO: Add validation
        return self._obj
