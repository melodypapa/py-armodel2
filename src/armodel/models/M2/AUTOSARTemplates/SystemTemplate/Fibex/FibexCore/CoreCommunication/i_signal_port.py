"""ISignalPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)


class ISignalPort(CommConnectorPort):
    """AUTOSAR ISignalPort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_filter", None, False, False, DataFilter),  # dataFilter
        ("dds_qos_profile", None, False, False, DdsCpQosProfile),  # ddsQosProfile
        ("first_timeout", None, True, False, None),  # firstTimeout
        ("handle_invalid_enum", None, False, False, HandleInvalidEnum),  # handleInvalidEnum
        ("timeout", None, True, False, None),  # timeout
    ]

    def __init__(self) -> None:
        """Initialize ISignalPort."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.dds_qos_profile: Optional[DdsCpQosProfile] = None
        self.first_timeout: Optional[TimeValue] = None
        self.handle_invalid_enum: Optional[HandleInvalidEnum] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalPort":
        """Create ISignalPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalPort since parent returns ARObject
        return cast("ISignalPort", obj)


class ISignalPortBuilder:
    """Builder for ISignalPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalPort = ISignalPort()

    def build(self) -> ISignalPort:
        """Build and return ISignalPort object.

        Returns:
            ISignalPort instance
        """
        # TODO: Add validation
        return self._obj
