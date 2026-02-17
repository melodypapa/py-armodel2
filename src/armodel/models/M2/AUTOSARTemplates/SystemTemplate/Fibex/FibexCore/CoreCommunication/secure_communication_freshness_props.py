"""SecureCommunicationFreshnessProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SecureCommunicationFreshnessProps(Identifiable):
    """AUTOSAR SecureCommunicationFreshnessProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "freshness": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # freshness
        "freshness_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # freshnessValue
        "use_freshness": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # useFreshness
    }

    def __init__(self) -> None:
        """Initialize SecureCommunicationFreshnessProps."""
        super().__init__()
        self.freshness: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.use_freshness: Optional[Boolean] = None


class SecureCommunicationFreshnessPropsBuilder:
    """Builder for SecureCommunicationFreshnessProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationFreshnessProps = SecureCommunicationFreshnessProps()

    def build(self) -> SecureCommunicationFreshnessProps:
        """Build and return SecureCommunicationFreshnessProps object.

        Returns:
            SecureCommunicationFreshnessProps instance
        """
        # TODO: Add validation
        return self._obj
