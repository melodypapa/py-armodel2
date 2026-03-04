"""IncludedDataTypeSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 600)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_IncludedDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
        AutosarDataType,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class IncludedDataTypeSet(ARObject):
    """AUTOSAR IncludedDataTypeSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INCLUDED-DATA-TYPE-SET"


    data_type_refs: list[ARRef]
    literal_prefix: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "DATA-TYPE-REFS": ("_POLYMORPHIC_LIST", "data_type_refs", ["AbstractImplementationDataType", "ApplicationArrayDataType", "ApplicationDataType", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ImplementationDataType"]),
        "LITERAL-PREFIX": lambda obj, elem: setattr(obj, "literal_prefix", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize IncludedDataTypeSet."""
        super().__init__()
        self.data_type_refs: list[ARRef] = []
        self.literal_prefix: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize IncludedDataTypeSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IncludedDataTypeSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_type_refs (list to container "DATA-TYPE-REFS")
        if self.data_type_refs:
            wrapper = ET.Element("DATA-TYPE-REFS")
            for item in self.data_type_refs:
                serialized = SerializationHelper.serialize_item(item, "AutosarDataType")
                if serialized is not None:
                    child_elem = ET.Element("DATA-TYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize literal_prefix
        if self.literal_prefix is not None:
            serialized = SerializationHelper.serialize_item(self.literal_prefix, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LITERAL-PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IncludedDataTypeSet":
        """Deserialize XML element to IncludedDataTypeSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IncludedDataTypeSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IncludedDataTypeSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-TYPE-REFS":
                for item_elem in child:
                    obj.data_type_refs.append(ARRef.deserialize(item_elem))
            elif tag == "LITERAL-PREFIX":
                setattr(obj, "literal_prefix", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class IncludedDataTypeSetBuilder(BuilderBase):
    """Builder for IncludedDataTypeSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IncludedDataTypeSet = IncludedDataTypeSet()


    def with_data_types(self, items: list[AutosarDataType]) -> "IncludedDataTypeSetBuilder":
        """Set data_types list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_types = list(items) if items else []
        return self

    def with_literal_prefix(self, value: Optional[Identifier]) -> "IncludedDataTypeSetBuilder":
        """Set literal_prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.literal_prefix = value
        return self


    def add_data_type(self, item: AutosarDataType) -> "IncludedDataTypeSetBuilder":
        """Add a single item to data_types list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_types.append(item)
        return self

    def clear_data_types(self) -> "IncludedDataTypeSetBuilder":
        """Clear all items from data_types list.

        Returns:
            self for method chaining
        """
        self._obj.data_types = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataType",
        "literalPrefix",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IncludedDataTypeSet:
        """Build and return the IncludedDataTypeSet instance with validation."""
        self._validate_instance()
        return self._obj