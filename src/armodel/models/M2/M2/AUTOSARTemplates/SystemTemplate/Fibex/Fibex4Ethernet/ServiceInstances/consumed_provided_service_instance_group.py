"""ConsumedProvidedServiceInstanceGroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """AUTOSAR ConsumedProvidedServiceInstanceGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "consumed_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (ConsumedService),
        ),  # consumedServices
        "provided_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (ProvidedService),
        ),  # providedServices
    }

    def __init__(self) -> None:
        """Initialize ConsumedProvidedServiceInstanceGroup."""
        super().__init__()
        self.consumed_services: list[Any] = []
        self.provided_services: list[Any] = []


class ConsumedProvidedServiceInstanceGroupBuilder:
    """Builder for ConsumedProvidedServiceInstanceGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedProvidedServiceInstanceGroup = ConsumedProvidedServiceInstanceGroup()

    def build(self) -> ConsumedProvidedServiceInstanceGroup:
        """Build and return ConsumedProvidedServiceInstanceGroup object.

        Returns:
            ConsumedProvidedServiceInstanceGroup instance
        """
        # TODO: Add validation
        return self._obj
