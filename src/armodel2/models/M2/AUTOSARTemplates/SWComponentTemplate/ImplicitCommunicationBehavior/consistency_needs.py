"""ConsistencyNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 221)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 178)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
        DataPrototypeGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
        RunnableEntityGroup,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ConsistencyNeeds(Identifiable):
    """AUTOSAR ConsistencyNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSISTENCY-NEEDS"


    dpg_does_not_refs: list[ARRef]
    dpg_require_refs: list[ARRef]
    reg_does_not_refs: list[ARRef]
    reg_require_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DPG-DOES-NOT-REFS": lambda obj, elem: [obj.dpg_does_not_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "DPG-REQUIRES-REFS": lambda obj, elem: [obj.dpg_require_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "REG-DOES-NOT-REFS": lambda obj, elem: [obj.reg_does_not_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "REG-REQUIRES-REFS": lambda obj, elem: [obj.reg_require_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize ConsistencyNeeds."""
        super().__init__()
        self.dpg_does_not_refs: list[ARRef] = []
        self.dpg_require_refs: list[ARRef] = []
        self.reg_does_not_refs: list[ARRef] = []
        self.reg_require_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ConsistencyNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsistencyNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dpg_does_not_refs (list to container "DPG-DOES-NOT-REFS")
        if self.dpg_does_not_refs:
            wrapper = ET.Element("DPG-DOES-NOT-REFS")
            for item in self.dpg_does_not_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    child_elem = ET.Element("DPG-DOES-NOT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dpg_require_refs (list to container "DPG-REQUIRES-REFS")
        if self.dpg_require_refs:
            wrapper = ET.Element("DPG-REQUIRES-REFS")
            for item in self.dpg_require_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    child_elem = ET.Element("DPG-REQUIRE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reg_does_not_refs (list to container "REG-DOES-NOT-REFS")
        if self.reg_does_not_refs:
            wrapper = ET.Element("REG-DOES-NOT-REFS")
            for item in self.reg_does_not_refs:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntityGroup")
                if serialized is not None:
                    child_elem = ET.Element("REG-DOES-NOT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reg_require_refs (list to container "REG-REQUIRES-REFS")
        if self.reg_require_refs:
            wrapper = ET.Element("REG-REQUIRES-REFS")
            for item in self.reg_require_refs:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntityGroup")
                if serialized is not None:
                    child_elem = ET.Element("REG-REQUIRE-REF")
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
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeeds":
        """Deserialize XML element to ConsistencyNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsistencyNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsistencyNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DPG-DOES-NOT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dpg_does_not_refs.append(ARRef.deserialize(item_elem))
            elif tag == "DPG-REQUIRES-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dpg_require_refs.append(ARRef.deserialize(item_elem))
            elif tag == "REG-DOES-NOT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.reg_does_not_refs.append(ARRef.deserialize(item_elem))
            elif tag == "REG-REQUIRES-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.reg_require_refs.append(ARRef.deserialize(item_elem))

        return obj



class ConsistencyNeedsBuilder(IdentifiableBuilder):
    """Builder for ConsistencyNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConsistencyNeeds = ConsistencyNeeds()


    def with_dpg_does_nots(self, items: list[DataPrototypeGroup]) -> "ConsistencyNeedsBuilder":
        """Set dpg_does_nots list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dpg_does_nots = list(items) if items else []
        return self

    def with_dpg_requireses(self, items: list[DataPrototypeGroup]) -> "ConsistencyNeedsBuilder":
        """Set dpg_requireses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dpg_requireses = list(items) if items else []
        return self

    def with_reg_does_nots(self, items: list[RunnableEntityGroup]) -> "ConsistencyNeedsBuilder":
        """Set reg_does_nots list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.reg_does_nots = list(items) if items else []
        return self

    def with_reg_requireses(self, items: list[RunnableEntityGroup]) -> "ConsistencyNeedsBuilder":
        """Set reg_requireses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.reg_requireses = list(items) if items else []
        return self


    def add_dpg_does_not(self, item: DataPrototypeGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to dpg_does_nots list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dpg_does_nots.append(item)
        return self

    def clear_dpg_does_nots(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from dpg_does_nots list.

        Returns:
            self for method chaining
        """
        self._obj.dpg_does_nots = []
        return self

    def add_dpg_requires(self, item: DataPrototypeGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to dpg_requireses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dpg_requireses.append(item)
        return self

    def clear_dpg_requireses(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from dpg_requireses list.

        Returns:
            self for method chaining
        """
        self._obj.dpg_requireses = []
        return self

    def add_reg_does_not(self, item: RunnableEntityGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to reg_does_nots list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.reg_does_nots.append(item)
        return self

    def clear_reg_does_nots(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from reg_does_nots list.

        Returns:
            self for method chaining
        """
        self._obj.reg_does_nots = []
        return self

    def add_reg_requires(self, item: RunnableEntityGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to reg_requireses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.reg_requireses.append(item)
        return self

    def clear_reg_requireses(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from reg_requireses list.

        Returns:
            self for method chaining
        """
        self._obj.reg_requireses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dpgDoesNot",
        "dpgRequires",
        "regDoesNot",
        "regRequires",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConsistencyNeeds:
        """Build and return the ConsistencyNeeds instance with validation."""
        self._validate_instance()
        return self._obj