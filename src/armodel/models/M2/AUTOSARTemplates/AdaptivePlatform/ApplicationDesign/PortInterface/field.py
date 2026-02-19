"""Field AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_ApplicationDesign_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class Field(AutosarDataPrototype):
    """AUTOSAR Field."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    has_getter: Optional[Boolean]
    has_notifier: Optional[Boolean]
    has_setter: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize Field."""
        super().__init__()
        self.has_getter: Optional[Boolean] = None
        self.has_notifier: Optional[Boolean] = None
        self.has_setter: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Field":
        """Deserialize XML element to Field object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Field object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Field, cls).deserialize(element)

        # Parse has_getter
        child = ARObject._find_child_element(element, "HAS-GETTER")
        if child is not None:
            has_getter_value = child.text
            obj.has_getter = has_getter_value

        # Parse has_notifier
        child = ARObject._find_child_element(element, "HAS-NOTIFIER")
        if child is not None:
            has_notifier_value = child.text
            obj.has_notifier = has_notifier_value

        # Parse has_setter
        child = ARObject._find_child_element(element, "HAS-SETTER")
        if child is not None:
            has_setter_value = child.text
            obj.has_setter = has_setter_value

        return obj



class FieldBuilder:
    """Builder for Field."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Field = Field()

    def build(self) -> Field:
        """Build and return Field object.

        Returns:
            Field instance
        """
        # TODO: Add validation
        return self._obj
