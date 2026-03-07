"""BswModeSwitchEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import instance_ref
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import BswScheduleEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs.mode_in_bsw_module_description_instance_ref import (
    ModeInBswModuleDescriptionInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswModeSwitchEvent(BswScheduleEvent):
    """AUTOSAR BswModeSwitchEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-MODE-SWITCH-EVENT"


    activation: Optional[ModeActivationKind]
    _mode_irefs: list[ModeInBswModuleDescriptionInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "ACTIVATION": lambda obj, elem: setattr(obj, "activation", ModeActivationKind.deserialize(elem)),
        "MODES-IREF": lambda obj, elem: obj._mode_irefs.append(SerializationHelper.deserialize_by_tag(elem, "ModeInBswModuleDescriptionInstanceRef")),
    }


    def __init__(self) -> None:
        """Initialize BswModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None
        self._mode_irefs: list[ModeInBswModuleDescriptionInstanceRef] = []
    @property
    @instance_ref(flatten=True, list_type='multi')
    def mode_irefs(self) -> list[ModeInBswModuleDescriptionInstanceRef]:
        """Get mode_irefs instance reference."""
        return self._mode_irefs

    @mode_irefs.setter
    def mode_irefs(self, value: list[ModeInBswModuleDescriptionInstanceRef]) -> None:
        """Set mode_irefs instance reference."""
        self._mode_irefs = value


    def serialize(self) -> ET.Element:
        """Serialize BswModeSwitchEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModeSwitchEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activation
        if self.activation is not None:
            serialized = SerializationHelper.serialize_item(self.activation, "ModeActivationKind")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTIVATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_irefs (list of instance references with multi-wrapper pattern)
        if self.mode_irefs:
            irefs_container = ET.Element("MODE-IREFS")
            for item in self.mode_irefs:
                serialized = SerializationHelper.serialize_item(item, "ModeInBswModuleDescriptionInstanceRef")
                if serialized is not None:
                    # Wrap each item in its own IREF wrapper
                    iref_wrapper = ET.Element("MODE-IREF")
                    # Flatten: append children of serialized element directly to iref wrapper
                    for child in serialized:
                        iref_wrapper.append(child)
                    irefs_container.append(iref_wrapper)
            elem.append(irefs_container)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSwitchEvent":
        """Deserialize XML element to BswModeSwitchEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeSwitchEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModeSwitchEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACTIVATION":
                setattr(obj, "activation", ModeActivationKind.deserialize(child))
            elif tag == "MODE-IREFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._mode_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeInBswModuleDescriptionInstanceRef"))

        return obj



class BswModeSwitchEventBuilder(BswScheduleEventBuilder):
    """Builder for BswModeSwitchEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModeSwitchEvent = BswModeSwitchEvent()


    def with_activation(self, value: Optional[ModeActivationKind]) -> "BswModeSwitchEventBuilder":
        """Set activation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.activation = value
        return self

    def with_modes(self, items: list[ModeInBswModuleDescriptionInstanceRef]) -> "BswModeSwitchEventBuilder":
        """Set modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.modes = list(items) if items else []
        return self


    def add_mode(self, item: ModeInBswModuleDescriptionInstanceRef) -> "BswModeSwitchEventBuilder":
        """Add a single item to modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.modes.append(item)
        return self

    def clear_modes(self) -> "BswModeSwitchEventBuilder":
        """Clear all items from modes list.

        Returns:
            self for method chaining
        """
        self._obj.modes = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "activation",
        "mode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswModeSwitchEvent:
        """Build and return the BswModeSwitchEvent instance with validation."""
        self._validate_instance()
        return self._obj