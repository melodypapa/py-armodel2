"""CycleCounter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import CommunicationCycleBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CycleCounter(CommunicationCycle):
    """AUTOSAR CycleCounter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CYCLE-COUNTER"


    cycle_counter: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "CYCLE-COUNTER": lambda obj, elem: setattr(obj, "cycle_counter", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize CycleCounter."""
        super().__init__()
        self.cycle_counter: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize CycleCounter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CycleCounter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cycle_counter
        if self.cycle_counter is not None:
            serialized = SerializationHelper.serialize_item(self.cycle_counter, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-COUNTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CycleCounter":
        """Deserialize XML element to CycleCounter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CycleCounter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CycleCounter, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CYCLE-COUNTER":
                setattr(obj, "cycle_counter", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class CycleCounterBuilder(CommunicationCycleBuilder):
    """Builder for CycleCounter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CycleCounter = CycleCounter()


    def with_cycle_counter(self, value: Optional[Integer]) -> "CycleCounterBuilder":
        """Set cycle_counter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cycle_counter = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "CycleCounter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CycleCounter:
        """Build and return the CycleCounter instance with validation."""
        self._validate_instance()
        return self._obj