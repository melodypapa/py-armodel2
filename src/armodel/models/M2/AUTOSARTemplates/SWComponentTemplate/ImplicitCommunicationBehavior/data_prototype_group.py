"""DataPrototypeGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 223)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataPrototypeGroup(Identifiable):
    """AUTOSAR DataPrototypeGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_prototype_group_group_in_composition_instance_ref_refs: list[ARRef]
    implicit_data_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeGroup."""
        super().__init__()
        self.data_prototype_group_group_in_composition_instance_ref_refs: list[ARRef] = []
        self.implicit_data_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeGroup":
        """Deserialize XML element to DataPrototypeGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_prototype_group_group_in_composition_instance_ref_refs (list)
        obj.data_prototype_group_group_in_composition_instance_ref_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-PROTOTYPE-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REFS"):
            data_prototype_group_group_in_composition_instance_ref_refs_value = ARObject._deserialize_by_tag(child, "DataPrototypeGroup")
            obj.data_prototype_group_group_in_composition_instance_ref_refs.append(data_prototype_group_group_in_composition_instance_ref_refs_value)

        # Parse implicit_data_refs (list)
        obj.implicit_data_refs = []
        for child in ARObject._find_all_child_elements(element, "IMPLICIT-DATAS"):
            implicit_data_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.implicit_data_refs.append(implicit_data_refs_value)

        return obj



class DataPrototypeGroupBuilder:
    """Builder for DataPrototypeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeGroup = DataPrototypeGroup()

    def build(self) -> DataPrototypeGroup:
        """Build and return DataPrototypeGroup object.

        Returns:
            DataPrototypeGroup instance
        """
        # TODO: Add validation
        return self._obj
