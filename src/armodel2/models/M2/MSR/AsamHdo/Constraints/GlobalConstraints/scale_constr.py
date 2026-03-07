"""ScaleConstr AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1003)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Limit,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ScaleConstr(ARObject):
    """AUTOSAR ScaleConstr."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SCALE-CONSTR"


    desc: Optional[MultiLanguageOverviewParagraph]
    lower_limit: Optional[Limit]
    short_label: Optional[Identifier]
    upper_limit: Optional[Limit]
    validity: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DESC": lambda obj, elem: setattr(obj, "desc", SerializationHelper.deserialize_by_tag(elem, "MultiLanguageOverviewParagraph")),
        "LOWER-LIMIT": lambda obj, elem: setattr(obj, "lower_limit", SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "UPPER-LIMIT": lambda obj, elem: setattr(obj, "upper_limit", SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "VALIDITY": lambda obj, elem: setattr(obj, "validity", SerializationHelper.deserialize_by_tag(elem, "any (ScaleConstrValidity)")),
    }


    def __init__(self) -> None:
        """Initialize ScaleConstr."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.lower_limit: Optional[Limit] = None
        self.short_label: Optional[Identifier] = None
        self.upper_limit: Optional[Limit] = None
        self.validity: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ScaleConstr to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ScaleConstr, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize desc
        if self.desc is not None:
            serialized = SerializationHelper.serialize_item(self.desc, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lower_limit
        if self.lower_limit is not None:
            serialized = SerializationHelper.serialize_item(self.lower_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_limit
        if self.upper_limit is not None:
            serialized = SerializationHelper.serialize_item(self.upper_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize validity
        if self.validity is not None:
            serialized = SerializationHelper.serialize_item(self.validity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIDITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ScaleConstr":
        """Deserialize XML element to ScaleConstr object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ScaleConstr object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ScaleConstr, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DESC":
                setattr(obj, "desc", SerializationHelper.deserialize_by_tag(child, "MultiLanguageOverviewParagraph"))
            elif tag == "LOWER-LIMIT":
                setattr(obj, "lower_limit", SerializationHelper.deserialize_by_tag(child, "Limit"))
            elif tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "UPPER-LIMIT":
                setattr(obj, "upper_limit", SerializationHelper.deserialize_by_tag(child, "Limit"))
            elif tag == "VALIDITY":
                setattr(obj, "validity", SerializationHelper.deserialize_by_tag(child, "any (ScaleConstrValidity)"))

        return obj



class ScaleConstrBuilder(BuilderBase):
    """Builder for ScaleConstr with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ScaleConstr = ScaleConstr()


    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "ScaleConstrBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'desc' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_lower_limit(self, value: Optional[Limit]) -> "ScaleConstrBuilder":
        """Set lower_limit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'lower_limit' is required and cannot be None")
        self._obj.lower_limit = value
        return self

    def with_short_label(self, value: Optional[Identifier]) -> "ScaleConstrBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'short_label' is required and cannot be None")
        self._obj.short_label = value
        return self

    def with_upper_limit(self, value: Optional[Limit]) -> "ScaleConstrBuilder":
        """Set upper_limit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'upper_limit' is required and cannot be None")
        self._obj.upper_limit = value
        return self

    def with_validity(self, value: Optional[Any]) -> "ScaleConstrBuilder":
        """Set validity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'validity' is required and cannot be None")
        self._obj.validity = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "desc",
        "lowerLimit",
        "shortLabel",
        "upperLimit",
        "validity",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ScaleConstr:
        """Build and return the ScaleConstr instance with validation."""
        self._validate_instance()
        return self._obj