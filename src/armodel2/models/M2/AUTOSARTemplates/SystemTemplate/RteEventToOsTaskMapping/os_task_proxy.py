"""OsTaskProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import (
    OsTaskPreemptabilityEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class OsTaskProxy(ARElement):
    """AUTOSAR OsTaskProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "OS-TASK-PROXY"


    period: Optional[TimeValue]
    preemptability: Optional[OsTaskPreemptabilityEnum]
    priority: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "PERIOD": lambda obj, elem: setattr(obj, "period", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "PREEMPTABILITY": lambda obj, elem: setattr(obj, "preemptability", OsTaskPreemptabilityEnum.deserialize(elem)),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize OsTaskProxy."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.preemptability: Optional[OsTaskPreemptabilityEnum] = None
        self.priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize OsTaskProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(OsTaskProxy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize period
        if self.period is not None:
            serialized = SerializationHelper.serialize_item(self.period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize preemptability
        if self.preemptability is not None:
            serialized = SerializationHelper.serialize_item(self.preemptability, "OsTaskPreemptabilityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREEMPTABILITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OsTaskProxy":
        """Deserialize XML element to OsTaskProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OsTaskProxy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(OsTaskProxy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PERIOD":
                setattr(obj, "period", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "PREEMPTABILITY":
                setattr(obj, "preemptability", OsTaskPreemptabilityEnum.deserialize(child))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class OsTaskProxyBuilder(ARElementBuilder):
    """Builder for OsTaskProxy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: OsTaskProxy = OsTaskProxy()


    def with_period(self, value: Optional[TimeValue]) -> "OsTaskProxyBuilder":
        """Set period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.period = value
        return self

    def with_preemptability(self, value: Optional[OsTaskPreemptabilityEnum]) -> "OsTaskProxyBuilder":
        """Set preemptability attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.preemptability = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "OsTaskProxyBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "period",
        "preemptability",
        "priority",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> OsTaskProxy:
        """Build and return the OsTaskProxy instance with validation."""
        self._validate_instance()
        return self._obj