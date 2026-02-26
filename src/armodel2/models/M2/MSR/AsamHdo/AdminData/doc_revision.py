"""DocRevision AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 293)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    NameToken,
    RevisionLabelString,
    String,
)
from armodel2.models.M2.MSR.AsamHdo.AdminData.modification import (
    Modification,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DocRevision(ARObject):
    """AUTOSAR DocRevision."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    date: DateTime
    issued_by: Optional[String]
    modifications: list[Modification]
    revision_label_string: Optional[RevisionLabelString]
    revision_label_p1: Optional[RevisionLabelString]
    revision_label_p2: Optional[RevisionLabelString]
    state: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DocRevision."""
        super().__init__()
        self.date: DateTime = None
        self.issued_by: Optional[String] = None
        self.modifications: list[Modification] = []
        self.revision_label_string: Optional[RevisionLabelString] = None
        self.revision_label_p1: Optional[RevisionLabelString] = None
        self.revision_label_p2: Optional[RevisionLabelString] = None
        self.state: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize DocRevision to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocRevision, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize date
        if self.date is not None:
            serialized = SerializationHelper.serialize_item(self.date, "DateTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize issued_by
        if self.issued_by is not None:
            serialized = SerializationHelper.serialize_item(self.issued_by, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ISSUED-BY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize modifications (list to container "MODIFICATIONS")
        if self.modifications:
            wrapper = ET.Element("MODIFICATIONS")
            for item in self.modifications:
                serialized = SerializationHelper.serialize_item(item, "Modification")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize revision_label_string
        if self.revision_label_string is not None:
            serialized = SerializationHelper.serialize_item(self.revision_label_string, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVISION-LABEL-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize revision_label_p1
        if self.revision_label_p1 is not None:
            serialized = SerializationHelper.serialize_item(self.revision_label_p1, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVISION-LABEL-P1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize revision_label_p2
        if self.revision_label_p2 is not None:
            serialized = SerializationHelper.serialize_item(self.revision_label_p2, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVISION-LABEL-P2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize state
        if self.state is not None:
            serialized = SerializationHelper.serialize_item(self.state, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocRevision":
        """Deserialize XML element to DocRevision object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocRevision object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocRevision, cls).deserialize(element)

        # Parse date
        child = SerializationHelper.find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse issued_by
        child = SerializationHelper.find_child_element(element, "ISSUED-BY")
        if child is not None:
            issued_by_value = child.text
            obj.issued_by = issued_by_value

        # Parse modifications (list from container "MODIFICATIONS")
        obj.modifications = []
        container = SerializationHelper.find_child_element(element, "MODIFICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.modifications.append(child_value)

        # Parse revision_label_string
        child = SerializationHelper.find_child_element(element, "REVISION-LABEL-STRING")
        if child is not None:
            revision_label_string_value = child.text
            obj.revision_label_string = revision_label_string_value

        # Parse revision_label_p1
        child = SerializationHelper.find_child_element(element, "REVISION-LABEL-P1")
        if child is not None:
            revision_label_p1_value = child.text
            obj.revision_label_p1 = revision_label_p1_value

        # Parse revision_label_p2
        child = SerializationHelper.find_child_element(element, "REVISION-LABEL-P2")
        if child is not None:
            revision_label_p2_value = child.text
            obj.revision_label_p2 = revision_label_p2_value

        # Parse state
        child = SerializationHelper.find_child_element(element, "STATE")
        if child is not None:
            state_value = child.text
            obj.state = state_value

        return obj



class DocRevisionBuilder(BuilderBase):
    """Builder for DocRevision with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DocRevision = DocRevision()


    def with_date(self, value: DateTime) -> "DocRevisionBuilder":
        """Set date attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.date = value
        return self

    def with_issued_by(self, value: Optional[String]) -> "DocRevisionBuilder":
        """Set issued_by attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.issued_by = value
        return self

    def with_modifications(self, items: list[Modification]) -> "DocRevisionBuilder":
        """Set modifications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.modifications = list(items) if items else []
        return self

    def with_revision_label_string(self, value: Optional[RevisionLabelString]) -> "DocRevisionBuilder":
        """Set revision_label_string attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.revision_label_string = value
        return self

    def with_revision_label_p1(self, value: Optional[RevisionLabelString]) -> "DocRevisionBuilder":
        """Set revision_label_p1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.revision_label_p1 = value
        return self

    def with_revision_label_p2(self, value: Optional[RevisionLabelString]) -> "DocRevisionBuilder":
        """Set revision_label_p2 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.revision_label_p2 = value
        return self

    def with_state(self, value: Optional[NameToken]) -> "DocRevisionBuilder":
        """Set state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.state = value
        return self


    def add_modification(self, item: Modification) -> "DocRevisionBuilder":
        """Add a single item to modifications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.modifications.append(item)
        return self

    def clear_modifications(self) -> "DocRevisionBuilder":
        """Clear all items from modifications list.

        Returns:
            self for method chaining
        """
        self._obj.modifications = []
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


    def build(self) -> DocRevision:
        """Build and return the DocRevision instance with validation."""
        self._validate_instance()
        pass
        return self._obj