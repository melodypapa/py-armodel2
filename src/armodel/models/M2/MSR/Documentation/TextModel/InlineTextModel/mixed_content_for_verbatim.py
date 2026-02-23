"""MixedContentForVerbatim AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 292)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
    Br,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class MixedContentForVerbatim(ARObject, ABC):
    """AUTOSAR MixedContentForVerbatim."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    br: Br
    e: EmphasisText
    tt: Tt
    xref: Xref
    def __init__(self) -> None:
        """Initialize MixedContentForVerbatim."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.tt: Tt = None
        self.xref: Xref = None

    def serialize(self) -> ET.Element:
        """Serialize MixedContentForVerbatim to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MixedContentForVerbatim, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize br
        if self.br is not None:
            serialized = SerializationHelper.serialize_item(self.br, "Br")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize e
        if self.e is not None:
            serialized = SerializationHelper.serialize_item(self.e, "EmphasisText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("E")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tt
        if self.tt is not None:
            serialized = SerializationHelper.serialize_item(self.tt, "Tt")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize xref
        if self.xref is not None:
            serialized = SerializationHelper.serialize_item(self.xref, "Xref")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForVerbatim":
        """Deserialize XML element to MixedContentForVerbatim object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MixedContentForVerbatim object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MixedContentForVerbatim, cls).deserialize(element)

        # Parse br
        child = SerializationHelper.find_child_element(element, "BR")
        if child is not None:
            br_value = SerializationHelper.deserialize_by_tag(child, "Br")
            obj.br = br_value

        # Parse e
        child = SerializationHelper.find_child_element(element, "E")
        if child is not None:
            e_value = SerializationHelper.deserialize_by_tag(child, "EmphasisText")
            obj.e = e_value

        # Parse tt
        child = SerializationHelper.find_child_element(element, "TT")
        if child is not None:
            tt_value = SerializationHelper.deserialize_by_tag(child, "Tt")
            obj.tt = tt_value

        # Parse xref
        child = SerializationHelper.find_child_element(element, "XREF")
        if child is not None:
            xref_value = SerializationHelper.deserialize_by_tag(child, "Xref")
            obj.xref = xref_value

        return obj



class MixedContentForVerbatimBuilder(BuilderBase, ABC):
    """Builder for MixedContentForVerbatim with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MixedContentForVerbatim = MixedContentForVerbatim()


    def with_br(self, value: Br) -> "MixedContentForVerbatimBuilder":
        """Set br attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.br = value
        return self

    def with_e(self, value: EmphasisText) -> "MixedContentForVerbatimBuilder":
        """Set e attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.e = value
        return self

    def with_tt(self, value: Tt) -> "MixedContentForVerbatimBuilder":
        """Set tt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tt = value
        return self

    def with_xref(self, value: Xref) -> "MixedContentForVerbatimBuilder":
        """Set xref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.xref = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    @abstractmethod
    def build(self) -> MixedContentForVerbatim:
        """Build and return the MixedContentForVerbatim instance (abstract)."""
        raise NotImplementedError