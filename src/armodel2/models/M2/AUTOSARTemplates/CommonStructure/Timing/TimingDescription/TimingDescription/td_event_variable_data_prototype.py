"""TDEventVariableDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import TDEventVfbPortBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventVariableDataPrototype(TDEventVfbPort):
    """AUTOSAR TDEventVariableDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-VARIABLE-DATA-PROTOTYPE"


    data_element_ref: Optional[ARRef]
    td_event_variable_type: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DATA-ELEMENT-REF": lambda obj, elem: setattr(obj, "data_element_ref", ARRef.deserialize(elem)),
        "TD-EVENT-VARIABLE-TYPE": lambda obj, elem: setattr(obj, "td_event_variable_type", SerializationHelper.deserialize_by_tag(elem, "any (TDEventVariableData)")),
    }


    def __init__(self) -> None:
        """Initialize TDEventVariableDataPrototype."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.td_event_variable_type: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventVariableDataPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventVariableDataPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_variable_type
        if self.td_event_variable_type is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_variable_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-VARIABLE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVariableDataPrototype":
        """Deserialize XML element to TDEventVariableDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventVariableDataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventVariableDataPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-ELEMENT-REF":
                setattr(obj, "data_element_ref", ARRef.deserialize(child))
            elif tag == "TD-EVENT-VARIABLE-TYPE":
                setattr(obj, "td_event_variable_type", SerializationHelper.deserialize_by_tag(child, "any (TDEventVariableData)"))

        return obj



class TDEventVariableDataPrototypeBuilder(TDEventVfbPortBuilder):
    """Builder for TDEventVariableDataPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventVariableDataPrototype = TDEventVariableDataPrototype()


    def with_data_element(self, value: Optional[VariableDataPrototype]) -> "TDEventVariableDataPrototypeBuilder":
        """Set data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_element' is required and cannot be None")
        self._obj.data_element = value
        return self

    def with_td_event_variable_type(self, value: Optional[Any]) -> "TDEventVariableDataPrototypeBuilder":
        """Set td_event_variable_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'td_event_variable_type' is required and cannot be None")
        self._obj.td_event_variable_type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataElement",
        "tdEventVariableType",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDEventVariableDataPrototype:
        """Build and return the TDEventVariableDataPrototype instance with validation."""
        self._validate_instance()
        return self._obj