"""CouplingPortShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 123)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import CouplingPortStructuralElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_fifo import (
    CouplingPortFifo,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPortShaper(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT-SHAPER"


    idle_slope: Optional[PositiveInteger]
    predecessor_fifo_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "IDLE-SLOPE": lambda obj, elem: setattr(obj, "idle_slope", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PREDECESSOR-FIFO-REF": lambda obj, elem: setattr(obj, "predecessor_fifo_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CouplingPortShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.predecessor_fifo_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortShaper to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortShaper, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize idle_slope
        if self.idle_slope is not None:
            serialized = SerializationHelper.serialize_item(self.idle_slope, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDLE-SLOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize predecessor_fifo_ref
        if self.predecessor_fifo_ref is not None:
            serialized = SerializationHelper.serialize_item(self.predecessor_fifo_ref, "CouplingPortFifo")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREDECESSOR-FIFO-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortShaper":
        """Deserialize XML element to CouplingPortShaper object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortShaper object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortShaper, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IDLE-SLOPE":
                setattr(obj, "idle_slope", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PREDECESSOR-FIFO-REF":
                setattr(obj, "predecessor_fifo_ref", ARRef.deserialize(child))

        return obj



class CouplingPortShaperBuilder(CouplingPortStructuralElementBuilder):
    """Builder for CouplingPortShaper with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPortShaper = CouplingPortShaper()


    def with_idle_slope(self, value: Optional[PositiveInteger]) -> "CouplingPortShaperBuilder":
        """Set idle_slope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.idle_slope = value
        return self

    def with_predecessor_fifo(self, value: CouplingPortFifo) -> "CouplingPortShaperBuilder":
        """Set predecessor_fifo attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.predecessor_fifo = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "predecessorFifo",
    }
    _OPTIONAL_ATTRIBUTES = {
        "idleSlope",
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
        if getattr(self._obj, "predecessorFifo", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'predecessorFifo' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'predecessorFifo' is None", UserWarning)


    def build(self) -> CouplingPortShaper:
        """Build and return the CouplingPortShaper instance with validation."""
        self._validate_instance()
        return self._obj