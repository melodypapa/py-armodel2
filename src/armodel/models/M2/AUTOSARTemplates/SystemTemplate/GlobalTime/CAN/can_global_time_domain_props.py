"""CanGlobalTimeDomainProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR CanGlobalTimeDomainProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("fup_data_id_list", None, True, False, None),  # fupDataIDList
        ("ofns_data_id_list", None, True, False, None),  # ofnsDataIDList
        ("ofs_data_id_list", None, True, False, None),  # ofsDataIDList
        ("sync_data_id_list", None, True, False, None),  # syncDataIDList
    ]

    def __init__(self) -> None:
        """Initialize CanGlobalTimeDomainProps."""
        super().__init__()
        self.fup_data_id_list: PositiveInteger = None
        self.ofns_data_id_list: PositiveInteger = None
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanGlobalTimeDomainProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanGlobalTimeDomainProps":
        """Create CanGlobalTimeDomainProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanGlobalTimeDomainProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanGlobalTimeDomainProps since parent returns ARObject
        return cast("CanGlobalTimeDomainProps", obj)


class CanGlobalTimeDomainPropsBuilder:
    """Builder for CanGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanGlobalTimeDomainProps = CanGlobalTimeDomainProps()

    def build(self) -> CanGlobalTimeDomainProps:
        """Build and return CanGlobalTimeDomainProps object.

        Returns:
            CanGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
