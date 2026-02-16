"""DdsCpServiceInstance AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)


class DdsCpServiceInstance(AbstractServiceInstance):
    """AUTOSAR DdsCpServiceInstance."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dds_field_reply", None, False, False, DdsCpTopic),  # ddsFieldReply
        ("dds_field", None, False, False, DdsCpTopic),  # ddsField
        ("dds_method", None, False, False, DdsCpTopic),  # ddsMethod
        ("dds_service_qos", None, False, False, DdsCpQosProfile),  # ddsServiceQos
        ("service_instance", None, True, False, None),  # serviceInstance
        ("service_interface", None, True, False, None),  # serviceInterface
    ]

    def __init__(self) -> None:
        """Initialize DdsCpServiceInstance."""
        super().__init__()
        self.dds_field_reply: Optional[DdsCpTopic] = None
        self.dds_field: Optional[DdsCpTopic] = None
        self.dds_method: Optional[DdsCpTopic] = None
        self.dds_service_qos: Optional[DdsCpQosProfile] = None
        self.service_instance: Optional[PositiveInteger] = None
        self.service_interface: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpServiceInstance to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpServiceInstance":
        """Create DdsCpServiceInstance from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpServiceInstance instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpServiceInstance since parent returns ARObject
        return cast("DdsCpServiceInstance", obj)


class DdsCpServiceInstanceBuilder:
    """Builder for DdsCpServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstance = DdsCpServiceInstance()

    def build(self) -> DdsCpServiceInstance:
        """Build and return DdsCpServiceInstance object.

        Returns:
            DdsCpServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
