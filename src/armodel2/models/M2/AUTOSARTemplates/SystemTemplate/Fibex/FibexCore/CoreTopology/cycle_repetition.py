"""CycleRepetition AUTOSAR element.

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
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CycleRepetitionType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CycleRepetition(CommunicationCycle):
    """AUTOSAR CycleRepetition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CYCLE-REPETITION"


    base_cycle: Optional[Integer]
    cycle_repetition: Optional[CycleRepetitionType]
    _DESERIALIZE_DISPATCH = {
        "BASE-CYCLE": lambda obj, elem: setattr(obj, "base_cycle", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "CYCLE-REPETITION": lambda obj, elem: setattr(obj, "cycle_repetition", CycleRepetitionType.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CycleRepetition."""
        super().__init__()
        self.base_cycle: Optional[Integer] = None
        self.cycle_repetition: Optional[CycleRepetitionType] = None

    def serialize(self) -> ET.Element:
        """Serialize CycleRepetition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CycleRepetition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_cycle
        if self.base_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.base_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cycle_repetition
        if self.cycle_repetition is not None:
            serialized = SerializationHelper.serialize_item(self.cycle_repetition, "CycleRepetitionType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-REPETITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CycleRepetition":
        """Deserialize XML element to CycleRepetition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CycleRepetition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CycleRepetition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-CYCLE":
                setattr(obj, "base_cycle", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "CYCLE-REPETITION":
                setattr(obj, "cycle_repetition", CycleRepetitionType.deserialize(child))

        return obj



class CycleRepetitionBuilder(CommunicationCycleBuilder):
    """Builder for CycleRepetition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CycleRepetition = CycleRepetition()


    def with_base_cycle(self, value: Optional[Integer]) -> "CycleRepetitionBuilder":
        """Set base_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base_cycle' is required and cannot be None")
        self._obj.base_cycle = value
        return self

    def with_cycle_repetition(self, value: Optional[CycleRepetitionType]) -> "CycleRepetitionBuilder":
        """Set cycle_repetition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'cycle_repetition' is required and cannot be None")
        self._obj.cycle_repetition = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "BaseCycle",
        "CycleRepetition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CycleRepetition:
        """Build and return the CycleRepetition instance with validation."""
        self._validate_instance()
        return self._obj