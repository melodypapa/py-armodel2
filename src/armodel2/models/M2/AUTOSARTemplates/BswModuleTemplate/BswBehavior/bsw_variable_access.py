"""BswVariableAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 81)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswVariableAccess(Referrable):
    """AUTOSAR BswVariableAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-VARIABLE-ACCESS"


    accessed_variable_ref: Optional[ARRef]
    context_limitation_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ACCESSED-VARIABLE-REF": lambda obj, elem: setattr(obj, "accessed_variable_ref", ARRef.deserialize(elem)),
        "CONTEXT-LIMITATION-REFS": lambda obj, elem: [obj.context_limitation_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize BswVariableAccess."""
        super().__init__()
        self.accessed_variable_ref: Optional[ARRef] = None
        self.context_limitation_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BswVariableAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswVariableAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accessed_variable_ref
        if self.accessed_variable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.accessed_variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESSED-VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_limitation_refs (list to container "CONTEXT-LIMITATION-REFS")
        if self.context_limitation_refs:
            wrapper = ET.Element("CONTEXT-LIMITATION-REFS")
            for item in self.context_limitation_refs:
                serialized = SerializationHelper.serialize_item(item, "BswDistinguishedPartition")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-LIMITATION-REF")
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
    def deserialize(cls, element: ET.Element) -> "BswVariableAccess":
        """Deserialize XML element to BswVariableAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswVariableAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswVariableAccess, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESSED-VARIABLE-REF":
                setattr(obj, "accessed_variable_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-LIMITATION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_limitation_refs.append(ARRef.deserialize(item_elem))

        return obj



class BswVariableAccessBuilder(ReferrableBuilder):
    """Builder for BswVariableAccess with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswVariableAccess = BswVariableAccess()


    def with_accessed_variable(self, value: Optional[VariableDataPrototype]) -> "BswVariableAccessBuilder":
        """Set accessed_variable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accessed_variable = value
        return self

    def with_context_limitations(self, items: list[BswDistinguishedPartition]) -> "BswVariableAccessBuilder":
        """Set context_limitations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_limitations = list(items) if items else []
        return self


    def add_context_limitation(self, item: BswDistinguishedPartition) -> "BswVariableAccessBuilder":
        """Add a single item to context_limitations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_limitations.append(item)
        return self

    def clear_context_limitations(self) -> "BswVariableAccessBuilder":
        """Clear all items from context_limitations list.

        Returns:
            self for method chaining
        """
        self._obj.context_limitations = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accessedVariable",
        "contextLimitation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswVariableAccess:
        """Build and return the BswVariableAccess instance with validation."""
        self._validate_instance()
        return self._obj