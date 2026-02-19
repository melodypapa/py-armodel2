"""InternalConstrs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 407)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MonotonyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.scale_constr import (
    ScaleConstr,
)


class InternalConstrs(ARObject):
    """AUTOSAR InternalConstrs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lower_limit: Optional[Limit]
    max_diff: Optional[Numerical]
    max_gradient: Optional[Numerical]
    monotony: Optional[MonotonyEnum]
    scale_constrs: list[ScaleConstr]
    upper_limit: Optional[Limit]
    def __init__(self) -> None:
        """Initialize InternalConstrs."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.max_diff: Optional[Numerical] = None
        self.max_gradient: Optional[Numerical] = None
        self.monotony: Optional[MonotonyEnum] = None
        self.scale_constrs: list[ScaleConstr] = []
        self.upper_limit: Optional[Limit] = None
    def serialize(self) -> ET.Element:
        """Serialize InternalConstrs to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize lower_limit
        if self.lower_limit is not None:
            serialized = ARObject._serialize_item(self.lower_limit, "Limit")
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

        # Serialize max_diff
        if self.max_diff is not None:
            serialized = ARObject._serialize_item(self.max_diff, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DIFF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_gradient
        if self.max_gradient is not None:
            serialized = ARObject._serialize_item(self.max_gradient, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-GRADIENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize monotony
        if self.monotony is not None:
            serialized = ARObject._serialize_item(self.monotony, "MonotonyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MONOTONY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scale_constrs (list to container "SCALE-CONSTRS")
        if self.scale_constrs:
            wrapper = ET.Element("SCALE-CONSTRS")
            for item in self.scale_constrs:
                serialized = ARObject._serialize_item(item, "ScaleConstr")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize upper_limit
        if self.upper_limit is not None:
            serialized = ARObject._serialize_item(self.upper_limit, "Limit")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalConstrs":
        """Deserialize XML element to InternalConstrs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalConstrs object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lower_limit
        child = ARObject._find_child_element(element, "LOWER-LIMIT")
        if child is not None:
            lower_limit_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.lower_limit = lower_limit_value

        # Parse max_diff
        child = ARObject._find_child_element(element, "MAX-DIFF")
        if child is not None:
            max_diff_value = child.text
            obj.max_diff = max_diff_value

        # Parse max_gradient
        child = ARObject._find_child_element(element, "MAX-GRADIENT")
        if child is not None:
            max_gradient_value = child.text
            obj.max_gradient = max_gradient_value

        # Parse monotony
        child = ARObject._find_child_element(element, "MONOTONY")
        if child is not None:
            monotony_value = MonotonyEnum.deserialize(child)
            obj.monotony = monotony_value

        # Parse scale_constrs (list from container "SCALE-CONSTRS")
        obj.scale_constrs = []
        container = ARObject._find_child_element(element, "SCALE-CONSTRS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.scale_constrs.append(child_value)

        # Parse upper_limit
        child = ARObject._find_child_element(element, "UPPER-LIMIT")
        if child is not None:
            upper_limit_value = ARObject._deserialize_by_tag(child, "Limit")
            obj.upper_limit = upper_limit_value

        return obj



class InternalConstrsBuilder:
    """Builder for InternalConstrs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalConstrs = InternalConstrs()

    def build(self) -> InternalConstrs:
        """Build and return InternalConstrs object.

        Returns:
            InternalConstrs instance
        """
        # TODO: Add validation
        return self._obj
