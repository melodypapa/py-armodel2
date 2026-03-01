"""RptHook AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 848)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptHook(ARObject):
    """AUTOSAR RptHook."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-HOOK"


    code_label: Optional[CIdentifier]
    mcd_identifier: Optional[NameToken]
    rpt_ar_hook: Optional[AtpFeature]
    sdgs: list[Sdg]
    _DESERIALIZE_DISPATCH = {
        "CODE-LABEL": lambda obj, elem: setattr(obj, "code_label", SerializationHelper.deserialize_by_tag(elem, "CIdentifier")),
        "MCD-IDENTIFIER": lambda obj, elem: setattr(obj, "mcd_identifier", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "RPT-AR-HOOK": ("_POLYMORPHIC", "rpt_ar_hook", ["AtpPrototype", "AtpStructureElement"]),
        "SDGS": lambda obj, elem: obj.sdgs.append(SerializationHelper.deserialize_by_tag(elem, "Sdg")),
    }


    def __init__(self) -> None:
        """Initialize RptHook."""
        super().__init__()
        self.code_label: Optional[CIdentifier] = None
        self.mcd_identifier: Optional[NameToken] = None
        self.rpt_ar_hook: Optional[AtpFeature] = None
        self.sdgs: list[Sdg] = []

    def serialize(self) -> ET.Element:
        """Serialize RptHook to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptHook, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize code_label
        if self.code_label is not None:
            serialized = SerializationHelper.serialize_item(self.code_label, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CODE-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mcd_identifier
        if self.mcd_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.mcd_identifier, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MCD-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_ar_hook
        if self.rpt_ar_hook is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_ar_hook, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-AR-HOOK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = SerializationHelper.serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptHook":
        """Deserialize XML element to RptHook object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptHook object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptHook, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CODE-LABEL":
                setattr(obj, "code_label", SerializationHelper.deserialize_by_tag(child, "CIdentifier"))
            elif tag == "MCD-IDENTIFIER":
                setattr(obj, "mcd_identifier", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "RPT-AR-HOOK":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-PROTOTYPE":
                        setattr(obj, "rpt_ar_hook", SerializationHelper.deserialize_by_tag(child[0], "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        setattr(obj, "rpt_ar_hook", SerializationHelper.deserialize_by_tag(child[0], "AtpStructureElement"))
            elif tag == "SDGS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.sdgs.append(SerializationHelper.deserialize_by_tag(item_elem, "Sdg"))

        return obj



class RptHookBuilder(BuilderBase):
    """Builder for RptHook with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptHook = RptHook()


    def with_code_label(self, value: Optional[CIdentifier]) -> "RptHookBuilder":
        """Set code_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.code_label = value
        return self

    def with_mcd_identifier(self, value: Optional[NameToken]) -> "RptHookBuilder":
        """Set mcd_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mcd_identifier = value
        return self

    def with_rpt_ar_hook(self, value: Optional[AtpFeature]) -> "RptHookBuilder":
        """Set rpt_ar_hook attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_ar_hook = value
        return self

    def with_sdgs(self, items: list[Sdg]) -> "RptHookBuilder":
        """Set sdgs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdgs = list(items) if items else []
        return self


    def add_sdg(self, item: Sdg) -> "RptHookBuilder":
        """Add a single item to sdgs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdgs.append(item)
        return self

    def clear_sdgs(self) -> "RptHookBuilder":
        """Clear all items from sdgs list.

        Returns:
            self for method chaining
        """
        self._obj.sdgs = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> RptHook:
        """Build and return the RptHook instance with validation."""
        self._validate_instance()
        pass
        return self._obj