"""CouplingPortFifo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import CouplingPortStructuralElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPortFifo(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortFifo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT-FIFO"


    assigned_traffic: PositiveInteger
    minimum_fifo: Optional[PositiveInteger]
    shaper: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "ASSIGNED-TRAFFIC": lambda obj, elem: setattr(obj, "assigned_traffic", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MINIMUM-FIFO": lambda obj, elem: setattr(obj, "minimum_fifo", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SHAPER": lambda obj, elem: setattr(obj, "shaper", SerializationHelper.deserialize_by_tag(elem, "any (CouplingPortAbstract)")),
    }


    def __init__(self) -> None:
        """Initialize CouplingPortFifo."""
        super().__init__()
        self.assigned_traffic: PositiveInteger = None
        self.minimum_fifo: Optional[PositiveInteger] = None
        self.shaper: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortFifo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortFifo, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_traffic
        if self.assigned_traffic is not None:
            serialized = SerializationHelper.serialize_item(self.assigned_traffic, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED-TRAFFIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_fifo
        if self.minimum_fifo is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_fifo, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-FIFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize shaper
        if self.shaper is not None:
            serialized = SerializationHelper.serialize_item(self.shaper, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHAPER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortFifo":
        """Deserialize XML element to CouplingPortFifo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortFifo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortFifo, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASSIGNED-TRAFFIC":
                setattr(obj, "assigned_traffic", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MINIMUM-FIFO":
                setattr(obj, "minimum_fifo", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SHAPER":
                setattr(obj, "shaper", SerializationHelper.deserialize_by_tag(child, "any (CouplingPortAbstract)"))

        return obj



class CouplingPortFifoBuilder(CouplingPortStructuralElementBuilder):
    """Builder for CouplingPortFifo with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPortFifo = CouplingPortFifo()


    def with_assigned_traffic(self, value: PositiveInteger) -> "CouplingPortFifoBuilder":
        """Set assigned_traffic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'assigned_traffic' is required and cannot be None")
        self._obj.assigned_traffic = value
        return self

    def with_minimum_fifo(self, value: Optional[PositiveInteger]) -> "CouplingPortFifoBuilder":
        """Set minimum_fifo attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minimum_fifo' is required and cannot be None")
        self._obj.minimum_fifo = value
        return self

    def with_shaper(self, value: Optional[Any]) -> "CouplingPortFifoBuilder":
        """Set shaper attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'shaper' is required and cannot be None")
        self._obj.shaper = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "assignedTraffic",
    }
    _OPTIONAL_ATTRIBUTES = {
        "minimumFifo",
        "shaper",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "assignedTraffic", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'assignedTraffic' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'assignedTraffic' is None", UserWarning)


    def build(self) -> CouplingPortFifo:
        """Build and return the CouplingPortFifo instance with validation."""
        self._validate_instance()
        return self._obj