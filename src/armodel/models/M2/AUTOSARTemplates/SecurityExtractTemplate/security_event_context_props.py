"""SecurityEventContextProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_definition import (
    SecurityEventDefinition,
)


class SecurityEventContextProps(Identifiable):
    """AUTOSAR SecurityEventContextProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_data", None, False, False, any (SecurityEventContext)),  # contextData
        ("default", None, False, False, any (SecurityEventReporting)),  # default
        ("persistent", None, True, False, None),  # persistent
        ("security_event", None, False, False, SecurityEventDefinition),  # securityEvent
        ("sensor_instance", None, True, False, None),  # sensorInstance
        ("severity", None, True, False, None),  # severity
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventContextProps."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.default: Optional[Any] = None
        self.persistent: Optional[Boolean] = None
        self.security_event: Optional[SecurityEventDefinition] = None
        self.sensor_instance: Optional[PositiveInteger] = None
        self.severity: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventContextProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextProps":
        """Create SecurityEventContextProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventContextProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventContextProps since parent returns ARObject
        return cast("SecurityEventContextProps", obj)


class SecurityEventContextPropsBuilder:
    """Builder for SecurityEventContextProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextProps = SecurityEventContextProps()

    def build(self) -> SecurityEventContextProps:
        """Build and return SecurityEventContextProps object.

        Returns:
            SecurityEventContextProps instance
        """
        # TODO: Add validation
        return self._obj
