"""DataConstrRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 405)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.internal_constrs import (
    InternalConstrs,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.phys_constrs import (
    PhysConstrs,
)


class DataConstrRule(ARObject):
    """AUTOSAR DataConstrRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    constr_level: Optional[Integer]
    internal_constrs: Optional[InternalConstrs]
    phys_constrs: Optional[PhysConstrs]
    def __init__(self) -> None:
        """Initialize DataConstrRule."""
        super().__init__()
        self.constr_level: Optional[Integer] = None
        self.internal_constrs: Optional[InternalConstrs] = None
        self.phys_constrs: Optional[PhysConstrs] = None

    def serialize(self) -> ET.Element:
        """Serialize DataConstrRule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataConstrRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constr_level
        if self.constr_level is not None:
            serialized = SerializationHelper.serialize_item(self.constr_level, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSTR-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize internal_constrs
        if self.internal_constrs is not None:
            serialized = SerializationHelper.serialize_item(self.internal_constrs, "InternalConstrs")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERNAL-CONSTRS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize phys_constrs
        if self.phys_constrs is not None:
            serialized = SerializationHelper.serialize_item(self.phys_constrs, "PhysConstrs")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYS-CONSTRS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataConstrRule":
        """Deserialize XML element to DataConstrRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataConstrRule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataConstrRule, cls).deserialize(element)

        # Parse constr_level
        child = SerializationHelper.find_child_element(element, "CONSTR-LEVEL")
        if child is not None:
            constr_level_value = child.text
            obj.constr_level = constr_level_value

        # Parse internal_constrs
        child = SerializationHelper.find_child_element(element, "INTERNAL-CONSTRS")
        if child is not None:
            internal_constrs_value = SerializationHelper.deserialize_by_tag(child, "InternalConstrs")
            obj.internal_constrs = internal_constrs_value

        # Parse phys_constrs
        child = SerializationHelper.find_child_element(element, "PHYS-CONSTRS")
        if child is not None:
            phys_constrs_value = SerializationHelper.deserialize_by_tag(child, "PhysConstrs")
            obj.phys_constrs = phys_constrs_value

        return obj



class DataConstrRuleBuilder:
    """Builder for DataConstrRule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataConstrRule = DataConstrRule()

    def build(self) -> DataConstrRule:
        """Build and return DataConstrRule object.

        Returns:
            DataConstrRule instance
        """
        # TODO: Add validation
        return self._obj
