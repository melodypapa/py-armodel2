"""DiagnosticIumprGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticIumprGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumprGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-IUMPR-GROUP"


    iumpr_refs: list[ARRef]
    iumpr_group_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "IUMPR-REFS": lambda obj, elem: [obj.iumpr_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "IUMPR-GROUP-REF": lambda obj, elem: setattr(obj, "iumpr_group_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticIumprGroup."""
        super().__init__()
        self.iumpr_refs: list[ARRef] = []
        self.iumpr_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIumprGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIumprGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize iumpr_refs (list to container "IUMPR-REFS")
        if self.iumpr_refs:
            wrapper = ET.Element("IUMPR-REFS")
            for item in self.iumpr_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticIumpr")
                if serialized is not None:
                    child_elem = ET.Element("IUMPR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize iumpr_group_ref
        if self.iumpr_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.iumpr_group_ref, "DiagnosticIumprGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IUMPR-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprGroup":
        """Deserialize XML element to DiagnosticIumprGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIumprGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IUMPR-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.iumpr_refs.append(ARRef.deserialize(item_elem))
            elif tag == "IUMPR-GROUP-REF":
                setattr(obj, "iumpr_group_ref", ARRef.deserialize(child))

        return obj



class DiagnosticIumprGroupBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticIumprGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticIumprGroup = DiagnosticIumprGroup()


    def with_iumprs(self, items: list[DiagnosticIumpr]) -> "DiagnosticIumprGroupBuilder":
        """Set iumprs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.iumprs = list(items) if items else []
        return self

    def with_iumpr_group(self, value: Optional[DiagnosticIumprGroup]) -> "DiagnosticIumprGroupBuilder":
        """Set iumpr_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iumpr_group = value
        return self


    def add_iumpr(self, item: DiagnosticIumpr) -> "DiagnosticIumprGroupBuilder":
        """Add a single item to iumprs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.iumprs.append(item)
        return self

    def clear_iumprs(self) -> "DiagnosticIumprGroupBuilder":
        """Clear all items from iumprs list.

        Returns:
            self for method chaining
        """
        self._obj.iumprs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "iumpr",
        "iumprGroup",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticIumprGroup:
        """Build and return the DiagnosticIumprGroup instance with validation."""
        self._validate_instance()
        return self._obj