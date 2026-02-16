"""SOMEIPTransformationISignalProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition_set import (
    TlvDataIdDefinitionSet,
)


class SOMEIPTransformationISignalProps(ARObject):
    """AUTOSAR SOMEIPTransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("implements", None, True, False, None),  # implements
        ("interface_version", None, True, False, None),  # interfaceVersion
        ("is_dynamic", None, True, False, None),  # isDynamic
        ("message_type", None, False, False, SOMEIPMessageTypeEnum),  # messageType
        ("size_of_array", None, True, False, None),  # sizeOfArray
        ("size_of_string", None, True, False, None),  # sizeOfString
        ("size_of_struct", None, True, False, None),  # sizeOfStruct
        ("size_of_union", None, True, False, None),  # sizeOfUnion
        ("tlv_data_ids", None, False, True, TlvDataIdDefinitionSet),  # tlvDataIds
    ]

    def __init__(self) -> None:
        """Initialize SOMEIPTransformationISignalProps."""
        super().__init__()
        self.implements: Optional[Boolean] = None
        self.interface_version: Optional[PositiveInteger] = None
        self.is_dynamic: Optional[Boolean] = None
        self.message_type: Optional[SOMEIPMessageTypeEnum] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None
        self.tlv_data_ids: list[TlvDataIdDefinitionSet] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SOMEIPTransformationISignalProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationISignalProps":
        """Create SOMEIPTransformationISignalProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SOMEIPTransformationISignalProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SOMEIPTransformationISignalProps since parent returns ARObject
        return cast("SOMEIPTransformationISignalProps", obj)


class SOMEIPTransformationISignalPropsBuilder:
    """Builder for SOMEIPTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationISignalProps = SOMEIPTransformationISignalProps()

    def build(self) -> SOMEIPTransformationISignalProps:
        """Build and return SOMEIPTransformationISignalProps object.

        Returns:
            SOMEIPTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
