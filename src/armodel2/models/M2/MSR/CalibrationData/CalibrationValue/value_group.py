"""ValueGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 458)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
        SwValues,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ValueGroup(ARObject):
    """AUTOSAR ValueGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VALUE-GROUP"


    label: Optional[MultilanguageLongName]
    vg_contents: Optional[SwValues]
    v: Optional[Numerical]
    vf: Optional[Numerical]
    vg: Optional[ValueGroup]
    vt: Optional[VerbatimString]
    vtf: Optional[NumericalOrText]
    _DESERIALIZE_DISPATCH = {
        "LABEL": lambda obj, elem: setattr(obj, "label", SerializationHelper.deserialize_by_tag(elem, "MultilanguageLongName")),
        "VG-CONTENTS": lambda obj, elem: setattr(obj, "vg_contents", SerializationHelper.deserialize_by_tag(elem, "SwValues")),
        "V": lambda obj, elem: setattr(obj, "v", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "VF": lambda obj, elem: setattr(obj, "vf", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "VG": lambda obj, elem: setattr(obj, "vg", SerializationHelper.deserialize_by_tag(elem, "ValueGroup")),
        "VT": lambda obj, elem: setattr(obj, "vt", SerializationHelper.deserialize_by_tag(elem, "VerbatimString")),
        "VTF": lambda obj, elem: setattr(obj, "vtf", SerializationHelper.deserialize_by_tag(elem, "NumericalOrText")),
    }


    def __init__(self) -> None:
        """Initialize ValueGroup."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.vg_contents: Optional[SwValues] = None
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vg: Optional[ValueGroup] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None

    def serialize(self) -> ET.Element:
        """Serialize ValueGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ValueGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vg_contents (atp_mixed - append children directly)
        if self.vg_contents is not None:
            serialized = SerializationHelper.serialize_item(self.vg_contents, "SwValues")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize v
        if self.v is not None:
            serialized = SerializationHelper.serialize_item(self.v, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vf
        if self.vf is not None:
            serialized = SerializationHelper.serialize_item(self.vf, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vg
        if self.vg is not None:
            serialized = SerializationHelper.serialize_item(self.vg, "ValueGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vt
        if self.vt is not None:
            serialized = SerializationHelper.serialize_item(self.vt, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vtf
        if self.vtf is not None:
            serialized = SerializationHelper.serialize_item(self.vtf, "NumericalOrText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VTF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueGroup":
        """Deserialize XML element to ValueGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ValueGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LABEL":
                setattr(obj, "label", SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName"))
            elif tag == "VG-CONTENTS":
                setattr(obj, "vg_contents", SerializationHelper.deserialize_by_tag(child, "SwValues"))
            elif tag == "V":
                setattr(obj, "v", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "VF":
                setattr(obj, "vf", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "VG":
                setattr(obj, "vg", SerializationHelper.deserialize_by_tag(child, "ValueGroup"))
            elif tag == "VT":
                setattr(obj, "vt", SerializationHelper.deserialize_by_tag(child, "VerbatimString"))
            elif tag == "VTF":
                setattr(obj, "vtf", SerializationHelper.deserialize_by_tag(child, "NumericalOrText"))

        return obj



class ValueGroupBuilder(BuilderBase):
    """Builder for ValueGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ValueGroup = ValueGroup()


    def with_label(self, value: Optional[MultilanguageLongName]) -> "ValueGroupBuilder":
        """Set label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'label' is required and cannot be None")
        self._obj.label = value
        return self

    def with_vg_contents(self, value: Optional[SwValues]) -> "ValueGroupBuilder":
        """Set vg_contents attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vg_contents' is required and cannot be None")
        self._obj.vg_contents = value
        return self

    def with_v(self, value: Optional[Numerical]) -> "ValueGroupBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'v' is required and cannot be None")
        self._obj.v = value
        return self

    def with_vf(self, value: Optional[Numerical]) -> "ValueGroupBuilder":
        """Set vf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vf' is required and cannot be None")
        self._obj.vf = value
        return self

    def with_vg(self, value: Optional[ValueGroup]) -> "ValueGroupBuilder":
        """Set vg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vg' is required and cannot be None")
        self._obj.vg = value
        return self

    def with_vt(self, value: Optional[VerbatimString]) -> "ValueGroupBuilder":
        """Set vt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vt' is required and cannot be None")
        self._obj.vt = value
        return self

    def with_vtf(self, value: Optional[NumericalOrText]) -> "ValueGroupBuilder":
        """Set vtf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vtf' is required and cannot be None")
        self._obj.vtf = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "label",
        "vgContents",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ValueGroup:
        """Build and return the ValueGroup instance with validation."""
        self._validate_instance()
        return self._obj