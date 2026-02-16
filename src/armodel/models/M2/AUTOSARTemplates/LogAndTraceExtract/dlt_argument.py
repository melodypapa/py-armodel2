"""DltArgument AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_argument import (
    DltArgument,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class DltArgument(Identifiable):
    """AUTOSAR DltArgument."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dlt_arguments", None, False, True, DltArgument),  # dltArguments
        ("length", None, True, False, None),  # length
        ("network", None, False, False, SwDataDefProps),  # network
        ("optional", None, True, False, None),  # optional
        ("predefined_text", None, True, False, None),  # predefinedText
        ("variable_length", None, True, False, None),  # variableLength
    ]

    def __init__(self) -> None:
        """Initialize DltArgument."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.length: Optional[PositiveInteger] = None
        self.network: Optional[SwDataDefProps] = None
        self.optional: Optional[Boolean] = None
        self.predefined_text: Optional[Boolean] = None
        self.variable_length: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DltArgument to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltArgument":
        """Create DltArgument from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DltArgument instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DltArgument since parent returns ARObject
        return cast("DltArgument", obj)


class DltArgumentBuilder:
    """Builder for DltArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltArgument = DltArgument()

    def build(self) -> DltArgument:
        """Build and return DltArgument object.

        Returns:
            DltArgument instance
        """
        # TODO: Add validation
        return self._obj
