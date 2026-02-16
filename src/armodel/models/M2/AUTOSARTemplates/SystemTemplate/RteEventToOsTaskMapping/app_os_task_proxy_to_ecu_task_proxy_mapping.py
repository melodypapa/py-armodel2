"""AppOsTaskProxyToEcuTaskProxyMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping.os_task_proxy import (
    OsTaskProxy,
)


class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """AUTOSAR AppOsTaskProxyToEcuTaskProxyMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("app_task_proxy", None, False, False, OsTaskProxy),  # appTaskProxy
        ("ecu_task_proxy", None, False, False, OsTaskProxy),  # ecuTaskProxy
        ("offset", None, True, False, None),  # offset
    ]

    def __init__(self) -> None:
        """Initialize AppOsTaskProxyToEcuTaskProxyMapping."""
        super().__init__()
        self.app_task_proxy: Optional[OsTaskProxy] = None
        self.ecu_task_proxy: Optional[OsTaskProxy] = None
        self.offset: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AppOsTaskProxyToEcuTaskProxyMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AppOsTaskProxyToEcuTaskProxyMapping":
        """Create AppOsTaskProxyToEcuTaskProxyMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AppOsTaskProxyToEcuTaskProxyMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AppOsTaskProxyToEcuTaskProxyMapping since parent returns ARObject
        return cast("AppOsTaskProxyToEcuTaskProxyMapping", obj)


class AppOsTaskProxyToEcuTaskProxyMappingBuilder:
    """Builder for AppOsTaskProxyToEcuTaskProxyMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AppOsTaskProxyToEcuTaskProxyMapping = AppOsTaskProxyToEcuTaskProxyMapping()

    def build(self) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """Build and return AppOsTaskProxyToEcuTaskProxyMapping object.

        Returns:
            AppOsTaskProxyToEcuTaskProxyMapping instance
        """
        # TODO: Add validation
        return self._obj
