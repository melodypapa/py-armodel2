"""FrGlobalTimeDomainProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR FrGlobalTimeDomainProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ofs_data_id_list", None, True, False, None),  # ofsDataIDList
        ("sync_data_id_list", None, True, False, None),  # syncDataIDList
    ]

    def __init__(self) -> None:
        """Initialize FrGlobalTimeDomainProps."""
        super().__init__()
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FrGlobalTimeDomainProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FrGlobalTimeDomainProps":
        """Create FrGlobalTimeDomainProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FrGlobalTimeDomainProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FrGlobalTimeDomainProps since parent returns ARObject
        return cast("FrGlobalTimeDomainProps", obj)


class FrGlobalTimeDomainPropsBuilder:
    """Builder for FrGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrGlobalTimeDomainProps = FrGlobalTimeDomainProps()

    def build(self) -> FrGlobalTimeDomainProps:
        """Build and return FrGlobalTimeDomainProps object.

        Returns:
            FrGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
