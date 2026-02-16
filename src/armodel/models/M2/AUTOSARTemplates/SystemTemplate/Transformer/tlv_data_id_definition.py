"""TlvDataIdDefinition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)


class TlvDataIdDefinition(ARObject):
    """AUTOSAR TlvDataIdDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("id", None, True, False, None),  # id
        ("tlv_argument", None, False, False, ArgumentDataPrototype),  # tlvArgument
        ("tlv", None, False, False, AbstractImplementationDataType),  # tlv
        ("tlv_record", None, False, False, any (ApplicationRecord)),  # tlvRecord
    ]

    def __init__(self) -> None:
        """Initialize TlvDataIdDefinition."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.tlv_argument: Optional[ArgumentDataPrototype] = None
        self.tlv: Optional[AbstractImplementationDataType] = None
        self.tlv_record: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TlvDataIdDefinition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinition":
        """Create TlvDataIdDefinition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TlvDataIdDefinition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TlvDataIdDefinition since parent returns ARObject
        return cast("TlvDataIdDefinition", obj)


class TlvDataIdDefinitionBuilder:
    """Builder for TlvDataIdDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlvDataIdDefinition = TlvDataIdDefinition()

    def build(self) -> TlvDataIdDefinition:
        """Build and return TlvDataIdDefinition object.

        Returns:
            TlvDataIdDefinition instance
        """
        # TODO: Add validation
        return self._obj
