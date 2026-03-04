"""SenderReceiverInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 335)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 94)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2054)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 244)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import DataInterfaceBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.invalidation_policy import (
    InvalidationPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item_set import (
    MetaDataItemSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderReceiverInterface(DataInterface):
    """AUTOSAR SenderReceiverInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SENDER-RECEIVER-INTERFACE"


    data_elements: list[VariableDataPrototype]
    invalidation_policy_policies: list[InvalidationPolicy]
    meta_data_item_sets: list[MetaDataItemSet]
    _DESERIALIZE_DISPATCH = {
        "DATA-ELEMENTS": lambda obj, elem: obj.data_elements.append(SerializationHelper.deserialize_by_tag(elem, "VariableDataPrototype")),
        "INVALIDATION-POLICY-POLICYS": lambda obj, elem: obj.invalidation_policy_policies.append(SerializationHelper.deserialize_by_tag(elem, "InvalidationPolicy")),
        "META-DATA-ITEM-SETS": lambda obj, elem: obj.meta_data_item_sets.append(SerializationHelper.deserialize_by_tag(elem, "MetaDataItemSet")),
    }


    def __init__(self) -> None:
        """Initialize SenderReceiverInterface."""
        super().__init__()
        self.data_elements: list[VariableDataPrototype] = []
        self.invalidation_policy_policies: list[InvalidationPolicy] = []
        self.meta_data_item_sets: list[MetaDataItemSet] = []

    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_elements (list to container "DATA-ELEMENTS")
        if self.data_elements:
            wrapper = ET.Element("DATA-ELEMENTS")
            for item in self.data_elements:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize invalidation_policy_policies (list to container "INVALIDATION-POLICY-POLICYS")
        if self.invalidation_policy_policies:
            wrapper = ET.Element("INVALIDATION-POLICY-POLICYS")
            for item in self.invalidation_policy_policies:
                serialized = SerializationHelper.serialize_item(item, "InvalidationPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize meta_data_item_sets (list to container "META-DATA-ITEM-SETS")
        if self.meta_data_item_sets:
            wrapper = ET.Element("META-DATA-ITEM-SETS")
            for item in self.meta_data_item_sets:
                serialized = SerializationHelper.serialize_item(item, "MetaDataItemSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverInterface":
        """Deserialize XML element to SenderReceiverInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverInterface, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableDataPrototype"))
            elif tag == "INVALIDATION-POLICY-POLICYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.invalidation_policy_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "InvalidationPolicy"))
            elif tag == "META-DATA-ITEM-SETS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.meta_data_item_sets.append(SerializationHelper.deserialize_by_tag(item_elem, "MetaDataItemSet"))

        return obj



class SenderReceiverInterfaceBuilder(DataInterfaceBuilder):
    """Builder for SenderReceiverInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderReceiverInterface = SenderReceiverInterface()


    def with_data_elements(self, items: list[VariableDataPrototype]) -> "SenderReceiverInterfaceBuilder":
        """Set data_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_elements = list(items) if items else []
        return self

    def with_invalidation_policy_policies(self, items: list[InvalidationPolicy]) -> "SenderReceiverInterfaceBuilder":
        """Set invalidation_policy_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.invalidation_policy_policies = list(items) if items else []
        return self

    def with_meta_data_item_sets(self, items: list[MetaDataItemSet]) -> "SenderReceiverInterfaceBuilder":
        """Set meta_data_item_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.meta_data_item_sets = list(items) if items else []
        return self


    def add_data_element(self, item: VariableDataPrototype) -> "SenderReceiverInterfaceBuilder":
        """Add a single item to data_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_elements.append(item)
        return self

    def clear_data_elements(self) -> "SenderReceiverInterfaceBuilder":
        """Clear all items from data_elements list.

        Returns:
            self for method chaining
        """
        self._obj.data_elements = []
        return self

    def add_invalidation_policy_policy(self, item: InvalidationPolicy) -> "SenderReceiverInterfaceBuilder":
        """Add a single item to invalidation_policy_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.invalidation_policy_policies.append(item)
        return self

    def clear_invalidation_policy_policies(self) -> "SenderReceiverInterfaceBuilder":
        """Clear all items from invalidation_policy_policies list.

        Returns:
            self for method chaining
        """
        self._obj.invalidation_policy_policies = []
        return self

    def add_meta_data_item_set(self, item: MetaDataItemSet) -> "SenderReceiverInterfaceBuilder":
        """Add a single item to meta_data_item_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.meta_data_item_sets.append(item)
        return self

    def clear_meta_data_item_sets(self) -> "SenderReceiverInterfaceBuilder":
        """Clear all items from meta_data_item_sets list.

        Returns:
            self for method chaining
        """
        self._obj.meta_data_item_sets = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataElement",
        "invalidationPolicyPolicy",
        "metaDataItemSet",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SenderReceiverInterface:
        """Build and return the SenderReceiverInterface instance with validation."""
        self._validate_instance()
        return self._obj