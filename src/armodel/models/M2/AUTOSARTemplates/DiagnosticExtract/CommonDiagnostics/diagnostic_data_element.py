"""DiagnosticDataElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class DiagnosticDataElement(Identifiable):
    """AUTOSAR DiagnosticDataElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("array_size", None, False, False, ArraySizeSemanticsEnum),  # arraySize
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("scaling_info_size", None, True, False, None),  # scalingInfoSize
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticDataElement."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.scaling_info_size: Optional[PositiveInteger] = None
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticDataElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataElement":
        """Create DiagnosticDataElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticDataElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticDataElement since parent returns ARObject
        return cast("DiagnosticDataElement", obj)


class DiagnosticDataElementBuilder:
    """Builder for DiagnosticDataElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataElement = DiagnosticDataElement()

    def build(self) -> DiagnosticDataElement:
        """Build and return DiagnosticDataElement object.

        Returns:
            DiagnosticDataElement instance
        """
        # TODO: Add validation
        return self._obj
