"""AtomicSwComponentType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)


class AtomicSwComponentType(SwComponentType):
    """AUTOSAR AtomicSwComponentType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "internal_behavior": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwcInternalBehavior,
        ),  # internalBehavior
        "symbol_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SymbolProps,
        ),  # symbolProps
    }

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
