"""EcucQuery AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query_expression import (
        EcucQueryExpression,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class EcucQuery(Identifiable):
    """AUTOSAR EcucQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-QUERY"


    ecuc_query: Optional[EcucQueryExpression]
    _DESERIALIZE_DISPATCH = {
        "ECUC-QUERY": lambda obj, elem: setattr(obj, "ecuc_query", SerializationHelper.deserialize_by_tag(elem, "EcucQueryExpression")),
    }


    def __init__(self) -> None:
        """Initialize EcucQuery."""
        super().__init__()
        self.ecuc_query: Optional[EcucQueryExpression] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucQuery to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucQuery, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_query
        if self.ecuc_query is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_query, "EcucQueryExpression")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-QUERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucQuery":
        """Deserialize XML element to EcucQuery object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucQuery object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucQuery, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ECUC-QUERY":
                setattr(obj, "ecuc_query", SerializationHelper.deserialize_by_tag(child, "EcucQueryExpression"))

        return obj



class EcucQueryBuilder(IdentifiableBuilder):
    """Builder for EcucQuery with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucQuery = EcucQuery()


    def with_ecuc_query(self, value: Optional[EcucQueryExpression]) -> "EcucQueryBuilder":
        """Set ecuc_query attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecuc_query = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ecucQuery",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucQuery:
        """Build and return the EcucQuery instance with validation."""
        self._validate_instance()
        return self._obj