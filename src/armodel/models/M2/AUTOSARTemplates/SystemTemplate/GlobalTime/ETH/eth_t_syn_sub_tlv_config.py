"""EthTSynSubTlvConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EthTSynSubTlvConfig(ARObject):
    """AUTOSAR EthTSynSubTlvConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ofs_sub_tlv", None, True, False, None),  # ofsSubTlv
        ("status_sub_tlv", None, True, False, None),  # statusSubTlv
        ("time_sub_tlv", None, True, False, None),  # timeSubTlv
        ("user_data_sub_tlv", None, True, False, None),  # userDataSubTlv
    ]

    def __init__(self) -> None:
        """Initialize EthTSynSubTlvConfig."""
        super().__init__()
        self.ofs_sub_tlv: Optional[Boolean] = None
        self.status_sub_tlv: Optional[Boolean] = None
        self.time_sub_tlv: Optional[Boolean] = None
        self.user_data_sub_tlv: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthTSynSubTlvConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTSynSubTlvConfig":
        """Create EthTSynSubTlvConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthTSynSubTlvConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthTSynSubTlvConfig since parent returns ARObject
        return cast("EthTSynSubTlvConfig", obj)


class EthTSynSubTlvConfigBuilder:
    """Builder for EthTSynSubTlvConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTSynSubTlvConfig = EthTSynSubTlvConfig()

    def build(self) -> EthTSynSubTlvConfig:
        """Build and return EthTSynSubTlvConfig object.

        Returns:
            EthTSynSubTlvConfig instance
        """
        # TODO: Add validation
        return self._obj
