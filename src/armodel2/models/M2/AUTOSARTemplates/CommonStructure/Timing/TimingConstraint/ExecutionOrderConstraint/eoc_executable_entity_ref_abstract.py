"""EOCExecutableEntityRefAbstract AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """AUTOSAR EOCExecutableEntityRefAbstract."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    direct_successor_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "DIRECT-SUCCESSOR-REFS": lambda obj, elem: [obj.direct_successor_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefAbstract."""
        super().__init__()
        self.direct_successor_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EOCExecutableEntityRefAbstract to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EOCExecutableEntityRefAbstract, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direct_successor_refs (list to container "DIRECT-SUCCESSOR-REFS")
        if self.direct_successor_refs:
            wrapper = ET.Element("DIRECT-SUCCESSOR-REFS")
            for item in self.direct_successor_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("DIRECT-SUCCESSOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefAbstract":
        """Deserialize XML element to EOCExecutableEntityRefAbstract object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRefAbstract object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCExecutableEntityRefAbstract, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIRECT-SUCCESSOR-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.direct_successor_refs.append(ARRef.deserialize(item_elem))

        return obj



class EOCExecutableEntityRefAbstractBuilder(IdentifiableBuilder):
    """Builder for EOCExecutableEntityRefAbstract with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EOCExecutableEntityRefAbstract = EOCExecutableEntityRefAbstract()


    def with_direct_successors(self, items: list[Any]) -> "EOCExecutableEntityRefAbstractBuilder":
        """Set direct_successors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.direct_successors = list(items) if items else []
        return self


    def add_direct_successor(self, item: Any) -> "EOCExecutableEntityRefAbstractBuilder":
        """Add a single item to direct_successors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.direct_successors.append(item)
        return self

    def clear_direct_successors(self) -> "EOCExecutableEntityRefAbstractBuilder":
        """Clear all items from direct_successors list.

        Returns:
            self for method chaining
        """
        self._obj.direct_successors = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "directSuccessor",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> EOCExecutableEntityRefAbstract:
        """Build and return the EOCExecutableEntityRefAbstract instance (abstract)."""
        raise NotImplementedError