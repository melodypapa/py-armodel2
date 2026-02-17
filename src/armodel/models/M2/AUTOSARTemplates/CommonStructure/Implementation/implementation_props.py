"""ImplementationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 86)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 287)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2033)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)


class ImplementationProps(Referrable):
    """AUTOSAR ImplementationProps."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "symbol": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbol
    }

    def __init__(self) -> None:
        """Initialize ImplementationProps."""
        super().__init__()
        self.symbol: Optional[CIdentifier] = None


class ImplementationPropsBuilder:
    """Builder for ImplementationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationProps = ImplementationProps()

    def build(self) -> ImplementationProps:
        """Build and return ImplementationProps object.

        Returns:
            ImplementationProps instance
        """
        # TODO: Add validation
        return self._obj
