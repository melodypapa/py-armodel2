"""SecureCommunicationPropsSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class SecureCommunicationPropsSet(FibexElement):
    """AUTOSAR SecureCommunicationPropsSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "authentications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SecureCommunication),
        ),  # authentications
        "freshness_propses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SecureCommunication),
        ),  # freshnessPropses
    }

    def __init__(self) -> None:
        """Initialize SecureCommunicationPropsSet."""
        super().__init__()
        self.authentications: list[Any] = []
        self.freshness_propses: list[Any] = []


class SecureCommunicationPropsSetBuilder:
    """Builder for SecureCommunicationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationPropsSet = SecureCommunicationPropsSet()

    def build(self) -> SecureCommunicationPropsSet:
        """Build and return SecureCommunicationPropsSet object.

        Returns:
            SecureCommunicationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
