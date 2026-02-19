"""AliasNameAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 175)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class AliasNameAssignment(ARObject):
    """AUTOSAR AliasNameAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flat_instance: Optional[FlatInstanceDescriptor]
    identifiable: Optional[Identifiable]
    label: Optional[MultilanguageLongName]
    short_label: Optional[String]
    def __init__(self) -> None:
        """Initialize AliasNameAssignment."""
        super().__init__()
        self.flat_instance: Optional[FlatInstanceDescriptor] = None
        self.identifiable: Optional[Identifiable] = None
        self.label: Optional[MultilanguageLongName] = None
        self.short_label: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameAssignment":
        """Deserialize XML element to AliasNameAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AliasNameAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse flat_instance
        child = ARObject._find_child_element(element, "FLAT-INSTANCE")
        if child is not None:
            flat_instance_value = ARObject._deserialize_by_tag(child, "FlatInstanceDescriptor")
            obj.flat_instance = flat_instance_value

        # Parse identifiable
        child = ARObject._find_child_element(element, "IDENTIFIABLE")
        if child is not None:
            identifiable_value = ARObject._deserialize_by_tag(child, "Identifiable")
            obj.identifiable = identifiable_value

        # Parse label
        child = ARObject._find_child_element(element, "LABEL")
        if child is not None:
            label_value = ARObject._deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class AliasNameAssignmentBuilder:
    """Builder for AliasNameAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameAssignment = AliasNameAssignment()

    def build(self) -> AliasNameAssignment:
        """Build and return AliasNameAssignment object.

        Returns:
            AliasNameAssignment instance
        """
        # TODO: Add validation
        return self._obj
