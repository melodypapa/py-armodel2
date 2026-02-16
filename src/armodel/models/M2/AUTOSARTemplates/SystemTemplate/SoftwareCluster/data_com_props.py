"""DataComProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)


class DataComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR DataComProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data", None, False, False, DataConsistencyPolicyEnum),  # data
        ("send_indication_enum", None, False, False, SendIndicationEnum),  # sendIndicationEnum
    ]

    def __init__(self) -> None:
        """Initialize DataComProps."""
        super().__init__()
        self.data: Optional[DataConsistencyPolicyEnum] = None
        self.send_indication_enum: Optional[SendIndicationEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataComProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataComProps":
        """Create DataComProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataComProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataComProps since parent returns ARObject
        return cast("DataComProps", obj)


class DataComPropsBuilder:
    """Builder for DataComProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataComProps = DataComProps()

    def build(self) -> DataComProps:
        """Build and return DataComProps object.

        Returns:
            DataComProps instance
        """
        # TODO: Add validation
        return self._obj
