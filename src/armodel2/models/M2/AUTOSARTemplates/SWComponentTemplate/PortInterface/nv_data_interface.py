"""NvDataInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 664)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2041)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import DataInterfaceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class NvDataInterface(DataInterface):
    """AUTOSAR NvDataInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NV-DATA-INTERFACE"


    nv_data_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "NV-DATA-REFS": lambda obj, elem: [obj.nv_data_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize NvDataInterface."""
        super().__init__()
        self.nv_data_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize NvDataInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvDataInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nv_data_refs (list to container "NV-DATA-REFS")
        if self.nv_data_refs:
            wrapper = ET.Element("NV-DATA-REFS")
            for item in self.nv_data_refs:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("NV-DATA-REF")
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
    def deserialize(cls, element: ET.Element) -> "NvDataInterface":
        """Deserialize XML element to NvDataInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvDataInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvDataInterface, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NV-DATA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.nv_data_refs.append(ARRef.deserialize(item_elem))

        return obj



class NvDataInterfaceBuilder(DataInterfaceBuilder):
    """Builder for NvDataInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvDataInterface = NvDataInterface()


    def with_nv_datas(self, items: list[VariableDataPrototype]) -> "NvDataInterfaceBuilder":
        """Set nv_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_datas = list(items) if items else []
        return self


    def add_nv_data(self, item: VariableDataPrototype) -> "NvDataInterfaceBuilder":
        """Add a single item to nv_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_datas.append(item)
        return self

    def clear_nv_datas(self) -> "NvDataInterfaceBuilder":
        """Clear all items from nv_datas list.

        Returns:
            self for method chaining
        """
        self._obj.nv_datas = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "nvData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> NvDataInterface:
        """Build and return the NvDataInterface instance with validation."""
        self._validate_instance()
        return self._obj