"""SwRecordLayoutGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 422)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2066)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    NameToken,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout import (
    AsamRecordLayoutSemantics,
    AxisIndexType,
    RecordLayoutIteratorPoint,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel2.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param_type import (
    SwGenericAxisParamType,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_v import (
    SwRecordLayoutV,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
        SwRecordLayout,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwRecordLayoutGroup(ARObject):
    """AUTOSAR SwRecordLayoutGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-RECORD-LAYOUT-GROUP"


    category: Optional[AsamRecordLayoutSemantics]
    desc: Optional[MultiLanguageOverviewParagraph]
    short_label: Optional[Identifier]
    sw_generic_axis_param_type_ref: Optional[ARRef]
    sw_record_layout_component: Optional[Identifier]
    sw_record_layout_group_axis: Optional[AxisIndexType]
    sw_record_layout_group_from: Optional[RecordLayoutIteratorPoint]
    sw_record_layout_group_to: Optional[RecordLayoutIteratorPoint]
    sw_record_layout_group_content_type: Optional[swRecordLayoutGroupContent]
    sw_record_layout: Optional[SwRecordLayout]
    sw_record_layout_group: Optional[SwRecordLayoutGroup]
    sw_record_layout_v: Optional[SwRecordLayoutV]
    sw_record_layout_group_index: Optional[NameToken]
    sw_record_layout_group_step: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "AsamRecordLayoutSemantics")),
        "DESC": lambda obj, elem: setattr(obj, "desc", SerializationHelper.deserialize_by_tag(elem, "MultiLanguageOverviewParagraph")),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SW-GENERIC-AXIS-PARAM-TYPE-REF": lambda obj, elem: setattr(obj, "sw_generic_axis_param_type_ref", ARRef.deserialize(elem)),
        "SW-RECORD-LAYOUT-COMPONENT": lambda obj, elem: setattr(obj, "sw_record_layout_component", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SW-RECORD-LAYOUT-GROUP-AXIS": lambda obj, elem: setattr(obj, "sw_record_layout_group_axis", SerializationHelper.deserialize_by_tag(elem, "AxisIndexType")),
        "SW-RECORD-LAYOUT-GROUP-FROM": lambda obj, elem: setattr(obj, "sw_record_layout_group_from", SerializationHelper.deserialize_by_tag(elem, "RecordLayoutIteratorPoint")),
        "SW-RECORD-LAYOUT-GROUP-TO": lambda obj, elem: setattr(obj, "sw_record_layout_group_to", SerializationHelper.deserialize_by_tag(elem, "RecordLayoutIteratorPoint")),
        "SW-RECORD-LAYOUT-GROUP-CONTENT-TYPE": lambda obj, elem: setattr(obj, "sw_record_layout_group_content_type", SerializationHelper.deserialize_by_tag(elem, "swRecordLayoutGroupContent")),
        "SW-RECORD-LAYOUT": lambda obj, elem: setattr(obj, "sw_record_layout", SerializationHelper.deserialize_by_tag(elem, "SwRecordLayout")),
        "SW-RECORD-LAYOUT-GROUP": lambda obj, elem: setattr(obj, "sw_record_layout_group", SerializationHelper.deserialize_by_tag(elem, "SwRecordLayoutGroup")),
        "SW-RECORD-LAYOUT-V": lambda obj, elem: setattr(obj, "sw_record_layout_v", SerializationHelper.deserialize_by_tag(elem, "SwRecordLayoutV")),
        "SW-RECORD-LAYOUT-GROUP-INDEX": lambda obj, elem: setattr(obj, "sw_record_layout_group_index", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "SW-RECORD-LAYOUT-GROUP-STEP": lambda obj, elem: setattr(obj, "sw_record_layout_group_step", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroup."""
        super().__init__()
        self.category: Optional[AsamRecordLayoutSemantics] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param_type_ref: Optional[ARRef] = None
        self.sw_record_layout_component: Optional[Identifier] = None
        self.sw_record_layout_group_axis: Optional[AxisIndexType] = None
        self.sw_record_layout_group_from: Optional[RecordLayoutIteratorPoint] = None
        self.sw_record_layout_group_to: Optional[RecordLayoutIteratorPoint] = None
        self.sw_record_layout_group_content_type: Optional[swRecordLayoutGroupContent] = None
        self.sw_record_layout: Optional[SwRecordLayout] = None
        self.sw_record_layout_group: Optional[SwRecordLayoutGroup] = None
        self.sw_record_layout_v: Optional[SwRecordLayoutV] = None
        self.sw_record_layout_group_index: Optional[NameToken] = None
        self.sw_record_layout_group_step: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize SwRecordLayoutGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwRecordLayoutGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "AsamRecordLayoutSemantics")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize sw_generic_axis_param_type_ref
        if self.sw_generic_axis_param_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_generic_axis_param_type_ref, "SwGenericAxisParamType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS-PARAM-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_component
        if self.sw_record_layout_component is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_component, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_axis
        if self.sw_record_layout_group_axis is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_axis, "AxisIndexType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_from
        if self.sw_record_layout_group_from is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_from, "RecordLayoutIteratorPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-FROM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_to
        if self.sw_record_layout_group_to is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_to, "RecordLayoutIteratorPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_content_type (atp_mixed - append children directly)
        if self.sw_record_layout_group_content_type is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_content_type, "swRecordLayoutGroupContent")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize sw_record_layout
        if self.sw_record_layout is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout, "SwRecordLayout")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group
        if self.sw_record_layout_group is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group, "SwRecordLayoutGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_v
        if self.sw_record_layout_v is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_v, "SwRecordLayoutV")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_index
        if self.sw_record_layout_group_index is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_index, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_step
        if self.sw_record_layout_group_step is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_step, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-STEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutGroup":
        """Deserialize XML element to SwRecordLayoutGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwRecordLayoutGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "AsamRecordLayoutSemantics"))
            elif tag == "DESC":
                setattr(obj, "desc", SerializationHelper.deserialize_by_tag(child, "MultiLanguageOverviewParagraph"))
            elif tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SW-GENERIC-AXIS-PARAM-TYPE-REF":
                setattr(obj, "sw_generic_axis_param_type_ref", ARRef.deserialize(child))
            elif tag == "SW-RECORD-LAYOUT-COMPONENT":
                setattr(obj, "sw_record_layout_component", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SW-RECORD-LAYOUT-GROUP-AXIS":
                setattr(obj, "sw_record_layout_group_axis", SerializationHelper.deserialize_by_tag(child, "AxisIndexType"))
            elif tag == "SW-RECORD-LAYOUT-GROUP-FROM":
                setattr(obj, "sw_record_layout_group_from", SerializationHelper.deserialize_by_tag(child, "RecordLayoutIteratorPoint"))
            elif tag == "SW-RECORD-LAYOUT-GROUP-TO":
                setattr(obj, "sw_record_layout_group_to", SerializationHelper.deserialize_by_tag(child, "RecordLayoutIteratorPoint"))
            elif tag == "SW-RECORD-LAYOUT-GROUP-CONTENT-TYPE":
                setattr(obj, "sw_record_layout_group_content_type", SerializationHelper.deserialize_by_tag(child, "swRecordLayoutGroupContent"))
            elif tag == "SW-RECORD-LAYOUT":
                setattr(obj, "sw_record_layout", SerializationHelper.deserialize_by_tag(child, "SwRecordLayout"))
            elif tag == "SW-RECORD-LAYOUT-GROUP":
                setattr(obj, "sw_record_layout_group", SerializationHelper.deserialize_by_tag(child, "SwRecordLayoutGroup"))
            elif tag == "SW-RECORD-LAYOUT-V":
                setattr(obj, "sw_record_layout_v", SerializationHelper.deserialize_by_tag(child, "SwRecordLayoutV"))
            elif tag == "SW-RECORD-LAYOUT-GROUP-INDEX":
                setattr(obj, "sw_record_layout_group_index", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "SW-RECORD-LAYOUT-GROUP-STEP":
                setattr(obj, "sw_record_layout_group_step", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class SwRecordLayoutGroupBuilder(BuilderBase):
    """Builder for SwRecordLayoutGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwRecordLayoutGroup = SwRecordLayoutGroup()


    def with_category(self, value: Optional[AsamRecordLayoutSemantics]) -> "SwRecordLayoutGroupBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'category' is required and cannot be None")
        self._obj.category = value
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SwRecordLayoutGroupBuilder":
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

    def with_short_label(self, value: Optional[Identifier]) -> "SwRecordLayoutGroupBuilder":
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

    def with_sw_generic_axis_param_type(self, value: Optional[SwGenericAxisParamType]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_generic_axis_param_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_generic_axis_param_type' is required and cannot be None")
        self._obj.sw_generic_axis_param_type = value
        return self

    def with_sw_record_layout_component(self, value: Optional[Identifier]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_component attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_component' is required and cannot be None")
        self._obj.sw_record_layout_component = value
        return self

    def with_sw_record_layout_group_axis(self, value: Optional[AxisIndexType]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_axis attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_group_axis' is required and cannot be None")
        self._obj.sw_record_layout_group_axis = value
        return self

    def with_sw_record_layout_group_from(self, value: Optional[RecordLayoutIteratorPoint]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_from attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_group_from' is required and cannot be None")
        self._obj.sw_record_layout_group_from = value
        return self

    def with_sw_record_layout_group_to(self, value: Optional[RecordLayoutIteratorPoint]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_group_to' is required and cannot be None")
        self._obj.sw_record_layout_group_to = value
        return self

    def with_sw_record_layout_group_content_type(self, value: Optional[swRecordLayoutGroupContent]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_content_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_group_content_type' is required and cannot be None")
        self._obj.sw_record_layout_group_content_type = value
        return self

    def with_sw_record_layout(self, value: Optional[SwRecordLayout]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout' is required and cannot be None")
        self._obj.sw_record_layout = value
        return self

    def with_sw_record_layout_group(self, value: Optional[SwRecordLayoutGroup]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_group' is required and cannot be None")
        self._obj.sw_record_layout_group = value
        return self

    def with_sw_record_layout_v(self, value: Optional[SwRecordLayoutV]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_v' is required and cannot be None")
        self._obj.sw_record_layout_v = value
        return self

    def with_sw_record_layout_group_index(self, value: Optional[NameToken]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_group_index' is required and cannot be None")
        self._obj.sw_record_layout_group_index = value
        return self

    def with_sw_record_layout_group_step(self, value: Optional[Integer]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_step attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record_layout_group_step' is required and cannot be None")
        self._obj.sw_record_layout_group_step = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "category",
        "desc",
        "shortLabel",
        "swGenericAxisParamType",
        "swRecordLayoutComponent",
        "swRecordLayoutGroupAxis",
        "swRecordLayoutGroupContentType",
        "swRecordLayoutGroupFrom",
        "swRecordLayoutGroupIndex",
        "swRecordLayoutGroupStep",
        "swRecordLayoutGroupTo",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwRecordLayoutGroup:
        """Build and return the SwRecordLayoutGroup instance with validation."""
        self._validate_instance()
        return self._obj