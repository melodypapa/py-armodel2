"""SomeipSdClientServiceInstanceConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)


class SomeipSdClientServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdClientServiceInstanceConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("initial_find_behavior", None, False, False, InitialSdDelayConfig),  # initialFindBehavior
        ("priority", None, True, False, None),  # priority
        ("service_find", None, True, False, None),  # serviceFind
    ]

    def __init__(self) -> None:
        """Initialize SomeipSdClientServiceInstanceConfig."""
        super().__init__()
        self.initial_find_behavior: Optional[InitialSdDelayConfig] = None
        self.priority: Optional[PositiveInteger] = None
        self.service_find: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SomeipSdClientServiceInstanceConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdClientServiceInstanceConfig":
        """Create SomeipSdClientServiceInstanceConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SomeipSdClientServiceInstanceConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SomeipSdClientServiceInstanceConfig since parent returns ARObject
        return cast("SomeipSdClientServiceInstanceConfig", obj)


class SomeipSdClientServiceInstanceConfigBuilder:
    """Builder for SomeipSdClientServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdClientServiceInstanceConfig = SomeipSdClientServiceInstanceConfig()

    def build(self) -> SomeipSdClientServiceInstanceConfig:
        """Build and return SomeipSdClientServiceInstanceConfig object.

        Returns:
            SomeipSdClientServiceInstanceConfig instance
        """
        # TODO: Add validation
        return self._obj
