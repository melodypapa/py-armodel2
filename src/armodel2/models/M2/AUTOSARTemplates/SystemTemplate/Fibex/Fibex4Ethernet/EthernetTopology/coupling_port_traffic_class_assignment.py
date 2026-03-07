"""CouplingPortTrafficClassAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPortTrafficClassAssignment(Referrable):
    """AUTOSAR CouplingPortTrafficClassAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT"


    priority: PositiveInteger
    traffic_class: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TRAFFIC-CLASS": lambda obj, elem: setattr(obj, "traffic_class", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize CouplingPortTrafficClassAssignment."""
        super().__init__()
        self.priority: PositiveInteger = None
        self.traffic_class: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortTrafficClassAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortTrafficClassAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize traffic_class
        if self.traffic_class is not None:
            serialized = SerializationHelper.serialize_item(self.traffic_class, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRAFFIC-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortTrafficClassAssignment":
        """Deserialize XML element to CouplingPortTrafficClassAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortTrafficClassAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortTrafficClassAssignment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TRAFFIC-CLASS":
                setattr(obj, "traffic_class", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CouplingPortTrafficClassAssignmentBuilder(ReferrableBuilder):
    """Builder for CouplingPortTrafficClassAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPortTrafficClassAssignment = CouplingPortTrafficClassAssignment()


    def with_priority(self, value: PositiveInteger) -> "CouplingPortTrafficClassAssignmentBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'priority' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_traffic_class(self, value: Optional[PositiveInteger]) -> "CouplingPortTrafficClassAssignmentBuilder":
        """Set traffic_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'traffic_class' is required and cannot be None")
        self._obj.traffic_class = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "priority",
    }
    _OPTIONAL_ATTRIBUTES = {
        "trafficClass",
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
        if getattr(self._obj, "priority", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'priority' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'priority' is None", UserWarning)


    def build(self) -> CouplingPortTrafficClassAssignment:
        """Build and return the CouplingPortTrafficClassAssignment instance with validation."""
        self._validate_instance()
        return self._obj