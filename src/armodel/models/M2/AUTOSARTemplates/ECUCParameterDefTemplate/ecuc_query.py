"""EcucQuery AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query_expression import (
        EcucQueryExpression,
    )



class EcucQuery(Identifiable):
    """AUTOSAR EcucQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_query: Optional[EcucQueryExpression]
    def __init__(self) -> None:
        """Initialize EcucQuery."""
        super().__init__()
        self.ecuc_query: Optional[EcucQueryExpression] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucQuery to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucQuery, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_query
        if self.ecuc_query is not None:
            serialized = ARObject._serialize_item(self.ecuc_query, "EcucQueryExpression")
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

        # Parse ecuc_query
        child = ARObject._find_child_element(element, "ECUC-QUERY")
        if child is not None:
            ecuc_query_value = ARObject._deserialize_by_tag(child, "EcucQueryExpression")
            obj.ecuc_query = ecuc_query_value

        return obj



class EcucQueryBuilder:
    """Builder for EcucQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucQuery = EcucQuery()

    def build(self) -> EcucQuery:
        """Build and return EcucQuery object.

        Returns:
            EcucQuery instance
        """
        # TODO: Add validation
        return self._obj
