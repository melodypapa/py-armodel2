"""DataPrototypeGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 223)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

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
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
        VariableDataPrototype,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class DataPrototypeGroup(Identifiable):
    """AUTOSAR DataPrototypeGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-PROTOTYPE-GROUP"


    data_prototype_group_group_in_composition_instance_ref: list[ARRef]
    implicit_data_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS": lambda obj, elem: [obj.data_prototype_group_group_in_composition_instance_ref.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "IMPLICIT-DATA-REFS": lambda obj, elem: [obj.implicit_data_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DataPrototypeGroup."""
        super().__init__()
        self.data_prototype_group_group_in_composition_instance_ref: list[ARRef] = []
        self.implicit_data_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_prototype_group_group_in_composition_instance_ref (list to container "DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS")
        if self.data_prototype_group_group_in_composition_instance_ref:
            wrapper = ET.Element("DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS")
            for item in self.data_prototype_group_group_in_composition_instance_ref:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    child_elem = ET.Element("DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize implicit_data_refs (list to container "IMPLICIT-DATA-REFS")
        if self.implicit_data_refs:
            wrapper = ET.Element("IMPLICIT-DATA-REFS")
            for item in self.implicit_data_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("IMPLICIT-DATA-REF")
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
    def deserialize(cls, element: ET.Element) -> "DataPrototypeGroup":
        """Deserialize XML element to DataPrototypeGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_prototype_group_group_in_composition_instance_ref.append(ARRef.deserialize(item_elem))
            elif tag == "IMPLICIT-DATA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.implicit_data_refs.append(ARRef.deserialize(item_elem))

        return obj



class DataPrototypeGroupBuilder(IdentifiableBuilder):
    """Builder for DataPrototypeGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataPrototypeGroup = DataPrototypeGroup()


    def with_data_prototype_group_group_in_composition_instance_refs(self, items: list[DataPrototypeGroup]) -> "DataPrototypeGroupBuilder":
        """Set data_prototype_group_group_in_composition_instance_refs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_prototype_group_group_in_composition_instance_refs = list(items) if items else []
        return self

    def with_implicit_datas(self, items: list[VariableDataPrototype]) -> "DataPrototypeGroupBuilder":
        """Set implicit_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.implicit_datas = list(items) if items else []
        return self


    def add_data_prototype_group_group_in_composition_instance_ref(self, item: DataPrototypeGroup) -> "DataPrototypeGroupBuilder":
        """Add a single item to data_prototype_group_group_in_composition_instance_refs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_prototype_group_group_in_composition_instance_refs.append(item)
        return self

    def clear_data_prototype_group_group_in_composition_instance_refs(self) -> "DataPrototypeGroupBuilder":
        """Clear all items from data_prototype_group_group_in_composition_instance_refs list.

        Returns:
            self for method chaining
        """
        self._obj.data_prototype_group_group_in_composition_instance_refs = []
        return self

    def add_implicit_data(self, item: VariableDataPrototype) -> "DataPrototypeGroupBuilder":
        """Add a single item to implicit_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.implicit_datas.append(item)
        return self

    def clear_implicit_datas(self) -> "DataPrototypeGroupBuilder":
        """Clear all items from implicit_datas list.

        Returns:
            self for method chaining
        """
        self._obj.implicit_datas = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataPrototypeGroupGroupInCompositionInstanceRef",
        "implicitData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DataPrototypeGroup:
        """Build and return the DataPrototypeGroup instance with validation."""
        self._validate_instance()
        return self._obj