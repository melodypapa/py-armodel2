"""SecurityEventFilterChain AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_one_every_n_filter import (
    SecurityEventOneEveryNFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_state_filter import (
    SecurityEventStateFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_threshold_filter import (
    SecurityEventThresholdFilter,
)


class SecurityEventFilterChain(IdsCommonElement):
    """AUTOSAR SecurityEventFilterChain."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("aggregation", None, False, False, any (SecurityEvent)),  # aggregation
        ("one_every_n", None, False, False, SecurityEventOneEveryNFilter),  # oneEveryN
        ("state", None, False, False, SecurityEventStateFilter),  # state
        ("threshold", None, False, False, SecurityEventThresholdFilter),  # threshold
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventFilterChain."""
        super().__init__()
        self.aggregation: Optional[Any] = None
        self.one_every_n: Optional[SecurityEventOneEveryNFilter] = None
        self.state: Optional[SecurityEventStateFilter] = None
        self.threshold: Optional[SecurityEventThresholdFilter] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventFilterChain to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventFilterChain":
        """Create SecurityEventFilterChain from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventFilterChain instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventFilterChain since parent returns ARObject
        return cast("SecurityEventFilterChain", obj)


class SecurityEventFilterChainBuilder:
    """Builder for SecurityEventFilterChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventFilterChain = SecurityEventFilterChain()

    def build(self) -> SecurityEventFilterChain:
        """Build and return SecurityEventFilterChain object.

        Returns:
            SecurityEventFilterChain instance
        """
        # TODO: Add validation
        return self._obj
