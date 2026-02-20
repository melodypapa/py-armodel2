"""Compu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 386)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import (
    CompuContent,
)
from armodel.serialization.name_converter import NameConverter
from armodel.serialization.model_factory import ModelFactory


class Compu(ARObject):
    """AUTOSAR Compu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_content: Optional[CompuContent]
    compu_default: Optional[CompuConst]
    def __init__(self) -> None:
        """Initialize Compu."""
        super().__init__()
        self.compu_content: Optional[CompuContent] = None
        self.compu_default: Optional[CompuConst] = None

    def serialize(self) -> ET.Element:
        """Serialize Compu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this Compu
        """
        # Delegate to parent's serialize - it handles all attributes correctly
        # including compu_content and compu_default
        return super(Compu, self).serialize()

    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML element to Compu.

        Handles CompuContent polymorphic types by using ModelFactory to resolve
        concrete subclasses like CompuScales. This ensures Compu.compu_content
        is properly populated with the correct concrete subclass.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Compu instance with compu_content properly set
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Compu, cls).deserialize(element)

        # Use ModelFactory for polymorphic type resolution
        factory = ModelFactory()
        if not factory.is_initialized():
            factory.load_mappings()

        # Find child elements that are CompuContent or CompuConst subclasses
        for child in element:
            child_tag = ARObject._strip_namespace(child.tag)
            concrete_class = factory.get_class(child_tag)

            if concrete_class:
                # Import base classes for type checking
                from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import CompuContent
                from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import CompuConst

                # Check if it's a CompuContent subclass (for compu_content)
                if isinstance(concrete_class, type) and issubclass(concrete_class, CompuContent):
                    obj.compu_content = ARObject._unwrap_primitive(concrete_class.deserialize(child))
                # Check if it's a CompuConst (for compu_default)
                elif isinstance(concrete_class, type) and issubclass(concrete_class, CompuConst):
                    obj.compu_default = ARObject._unwrap_primitive(concrete_class.deserialize(child))

        return obj


class CompuBuilder:
    """Builder for Compu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Compu = Compu()

    def build(self) -> Compu:
        """Build and return Compu object.

        Returns:
            Compu instance
        """
        # TODO: Add validation
        return self._obj
