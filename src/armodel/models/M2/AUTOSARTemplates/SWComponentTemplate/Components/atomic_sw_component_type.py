"""AtomicSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 304)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 205)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)
from abc import ABC, abstractmethod


class AtomicSwComponentType(SwComponentType, ABC):
    """AUTOSAR AtomicSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    internal_behavior: Optional[SwcInternalBehavior]
    symbol_props: Optional[SymbolProps]
    def __init__(self) -> None:
        """Initialize AtomicSwComponentType."""
        super().__init__()
        self.internal_behavior: Optional[SwcInternalBehavior] = None
        self.symbol_props: Optional[SymbolProps] = None


class AtomicSwComponentTypeBuilder:
    """Builder for AtomicSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtomicSwComponentType = AtomicSwComponentType()

    def build(self) -> AtomicSwComponentType:
        """Build and return AtomicSwComponentType object.

        Returns:
            AtomicSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
