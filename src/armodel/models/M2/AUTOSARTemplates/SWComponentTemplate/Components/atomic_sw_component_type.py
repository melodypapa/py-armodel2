"""AtomicSwComponentType AUTOSAR element."""

from typing import Optional, cast
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


class AtomicSwComponentType(SwComponentType):
    """AUTOSAR AtomicSwComponentType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("internal_behavior", None, False, False, SwcInternalBehavior),  # internalBehavior
        ("symbol_props", None, False, False, SymbolProps),  # symbolProps
    ]

    def __init__(self) -> None:
        """Initialize AtomicSwComponentType."""
        super().__init__()
        self.internal_behavior: Optional[SwcInternalBehavior] = None
        self.symbol_props: Optional[SymbolProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AtomicSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtomicSwComponentType":
        """Create AtomicSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AtomicSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AtomicSwComponentType since parent returns ARObject
        return cast("AtomicSwComponentType", obj)


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
