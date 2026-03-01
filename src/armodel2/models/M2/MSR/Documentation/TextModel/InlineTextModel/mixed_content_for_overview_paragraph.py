"""MixedContentForOverviewParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 289)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
    Br,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.index_entry import (
    IndexEntry,
)
from armodel2.models.M2.MSR.Documentation.TextModel.SingleLanguageData.sl_overview_paragraph import (
    SlOverviewParagraph,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref_target import (
    XrefTarget,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MixedContentForOverviewParagraph(ARObject, ABC):
    """AUTOSAR MixedContentForOverviewParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    br: Br
    e: EmphasisText
    ft: SlOverviewParagraph
    ie: IndexEntry
    sub: Superscript
    sup: Superscript
    trace_ref: ARRef
    tt: Tt
    xref: Xref
    xref_target: XrefTarget
    _DESERIALIZE_DISPATCH = {
        "BR": lambda obj, elem: setattr(obj, "br", SerializationHelper.deserialize_by_tag(elem, "Br")),
        "E": lambda obj, elem: setattr(obj, "e", SerializationHelper.deserialize_by_tag(elem, "EmphasisText")),
        "FT": lambda obj, elem: setattr(obj, "ft", SerializationHelper.deserialize_by_tag(elem, "SlOverviewParagraph")),
        "IE": lambda obj, elem: setattr(obj, "ie", SerializationHelper.deserialize_by_tag(elem, "IndexEntry")),
        "SUB": lambda obj, elem: setattr(obj, "sub", SerializationHelper.deserialize_by_tag(elem, "Superscript")),
        "SUP": lambda obj, elem: setattr(obj, "sup", SerializationHelper.deserialize_by_tag(elem, "Superscript")),
        "TRACE-REF": ("_POLYMORPHIC", "trace_ref", ["AgeConstraint", "ArbitraryEventTriggering", "BurstPatternEventTriggering", "ConcretePatternEventTriggering", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "LatencyTimingConstraint", "OffsetTimingConstraint", "PeriodicEventTriggering", "SporadicEventTriggering", "StructuredReq", "SynchronizationPointConstraint", "TimingConstraint", "TraceableTable", "TraceableText"]),
        "TT": lambda obj, elem: setattr(obj, "tt", SerializationHelper.deserialize_by_tag(elem, "Tt")),
        "XREF": lambda obj, elem: setattr(obj, "xref", SerializationHelper.deserialize_by_tag(elem, "Xref")),
        "XREF-TARGET": lambda obj, elem: setattr(obj, "xref_target", SerializationHelper.deserialize_by_tag(elem, "XrefTarget")),
    }


    def __init__(self) -> None:
        """Initialize MixedContentForOverviewParagraph."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.ft: SlOverviewParagraph = None
        self.ie: IndexEntry = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.trace_ref: ARRef = None
        self.tt: Tt = None
        self.xref: Xref = None
        self.xref_target: XrefTarget = None

    def serialize(self) -> ET.Element:
        """Serialize MixedContentForOverviewParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MixedContentForOverviewParagraph, self).serialize()

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

        # Serialize ft
        if self.ft is not None:
            serialized = SerializationHelper.serialize_item(self.ft, "SlOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ie
        if self.ie is not None:
            serialized = SerializationHelper.serialize_item(self.ie, "IndexEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub
        if self.sub is not None:
            serialized = SerializationHelper.serialize_item(self.sub, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sup
        if self.sup is not None:
            serialized = SerializationHelper.serialize_item(self.sup, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trace_ref
        if self.trace_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trace_ref, "Traceable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRACE-REF")
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

        # Serialize xref_target
        if self.xref_target is not None:
            serialized = SerializationHelper.serialize_item(self.xref_target, "XrefTarget")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XREF-TARGET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForOverviewParagraph":
        """Deserialize XML element to MixedContentForOverviewParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MixedContentForOverviewParagraph object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MixedContentForOverviewParagraph, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BR":
                setattr(obj, "br", SerializationHelper.deserialize_by_tag(child, "Br"))
            elif tag == "E":
                setattr(obj, "e", SerializationHelper.deserialize_by_tag(child, "EmphasisText"))
            elif tag == "FT":
                setattr(obj, "ft", SerializationHelper.deserialize_by_tag(child, "SlOverviewParagraph"))
            elif tag == "IE":
                setattr(obj, "ie", SerializationHelper.deserialize_by_tag(child, "IndexEntry"))
            elif tag == "SUB":
                setattr(obj, "sub", SerializationHelper.deserialize_by_tag(child, "Superscript"))
            elif tag == "SUP":
                setattr(obj, "sup", SerializationHelper.deserialize_by_tag(child, "Superscript"))
            elif tag == "TRACE-REF":
                setattr(obj, "trace_ref", ARRef.deserialize(child))
            elif tag == "TT":
                setattr(obj, "tt", SerializationHelper.deserialize_by_tag(child, "Tt"))
            elif tag == "XREF":
                setattr(obj, "xref", SerializationHelper.deserialize_by_tag(child, "Xref"))
            elif tag == "XREF-TARGET":
                setattr(obj, "xref_target", SerializationHelper.deserialize_by_tag(child, "XrefTarget"))

        return obj



class MixedContentForOverviewParagraphBuilder(BuilderBase, ABC):
    """Builder for MixedContentForOverviewParagraph with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MixedContentForOverviewParagraph = MixedContentForOverviewParagraph()


    def with_br(self, value: Br) -> "MixedContentForOverviewParagraphBuilder":
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

    def with_e(self, value: EmphasisText) -> "MixedContentForOverviewParagraphBuilder":
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

    def with_ft(self, value: SlOverviewParagraph) -> "MixedContentForOverviewParagraphBuilder":
        """Set ft attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ft = value
        return self

    def with_ie(self, value: IndexEntry) -> "MixedContentForOverviewParagraphBuilder":
        """Set ie attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ie = value
        return self

    def with_sub(self, value: Superscript) -> "MixedContentForOverviewParagraphBuilder":
        """Set sub attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sub = value
        return self

    def with_sup(self, value: Superscript) -> "MixedContentForOverviewParagraphBuilder":
        """Set sup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sup = value
        return self

    def with_trace(self, value: Traceable) -> "MixedContentForOverviewParagraphBuilder":
        """Set trace attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.trace = value
        return self

    def with_tt(self, value: Tt) -> "MixedContentForOverviewParagraphBuilder":
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

    def with_xref(self, value: Xref) -> "MixedContentForOverviewParagraphBuilder":
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

    def with_xref_target(self, value: XrefTarget) -> "MixedContentForOverviewParagraphBuilder":
        """Set xref_target attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.xref_target = value
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


    @abstractmethod
    def build(self) -> MixedContentForOverviewParagraph:
        """Build and return the MixedContentForOverviewParagraph instance (abstract)."""
        raise NotImplementedError